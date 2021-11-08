from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return {tuple(int(pos) for pos in elem[0].replace('/dev/grid/node-x', '').replace('y', '').split('-')) : {'size': int(elem[1][:-1]), 'used': int(elem[2][:-1]), 'available': int(elem[3][:-1]), 'use': int(elem[4][:-1])} for elem in [i.strip().split() for i in f.readlines() if i.startswith('/')]}


class Tree:
    def __init__(self, scheme: dict, firstNode):
        # Données du problème
        self.states = defaultdict(lambda: inf)
        # Données relatives à l'arbre
        self.bestValue = inf
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
        self.states[firstNode.state] = firstNode.moves
        self.scheme = scheme
        self.unemptiable_nodes = self.search_unemptiable_nodes()
    
    def search_unemptiable_nodes(self):
        unemptiable_nodes = list()
        for key_A, value_A in self.scheme.items():
            if value_A['used'] != 0:
                explorable_nodes = [tuple((key_A[0] + xDelta, key_A[1] + yDelta)) for xDelta in range(-1, 2) for yDelta in range(-1, 2) if xDelta**2 + yDelta**2 == 1 and tuple((key_A[0] + xDelta, key_A[1] + yDelta)) in self.scheme]
                if value_A['used'] > max(scheme[explorable_node]['size'] for explorable_node in explorable_nodes):
                    unemptiable_nodes.append(key_A)
        
        return unemptiable_nodes

    
    def expandTree(self):
        currentNode = self.openNodes.popleft() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.moves < self.bestValue and currentNode.state[0] == (0, 0): # Définir ici la condition de succès
            self.bestValue = currentNode.moves
        else:
            for son in currentNode.reachableNodes(currentNode, self.scheme):
                if son.moves < min(self.bestValue, self.states[son.state]):
                    self.states[son.state] = son.moves
                    self.openNodes.append(son)


class Node:
    def __init__(self, departure_data_pos: tuple, zero_data_pos: tuple, moves: int):
        self.moves = moves
        self.state = (departure_data_pos, zero_data_pos) # Définir ici comment qualifier un noeud avec un état unique
    
    def reachableNodes(self, currentNode, scheme):
        # Définir ici comment rechercher les prochains noeuds
        emptiable_nodes = [tuple((currentNode.state[1][0] + xDelta, currentNode.state[1][1] + yDelta)) for xDelta in range(-1, 2) for yDelta in range(-1, 2) if xDelta**2 + yDelta**2 == 1 and tuple((currentNode.state[1][0] + xDelta, currentNode.state[1][1] + yDelta)) in scheme]
        for emptiable_node in emptiable_nodes:
            if scheme[emptiable_node]['used'] <= scheme[currentNode.state[1]]['size']:
                next_departure_data_pos = currentNode.state[1] if emptiable_node == currentNode.state[0] else currentNode.state[0]
                yield Node(next_departure_data_pos, emptiable_node, currentNode.moves + 1)
        

# def emptiable_node(scheme: dict):
#     emptiable_node_amount = 0
#     for key_A, value_A in scheme.items():
#         if value_A['used'] != 0:
#             explorable_nodes = [tuple((key_A[0] + xDelta, key_A[1] + yDelta)) for xDelta in range(-1, 2) for yDelta in range(-1, 2) if xDelta**2 + yDelta**2 == 1 and tuple((key_A[0] + xDelta, key_A[1] + yDelta)) in scheme]
#             for explorable_node in explorable_nodes:
#                 if value_A['used'] <= scheme[explorable_node]['available']:
#                     emptiable_node_amount += 1
#                     print(key_A, explorable_node)
#                     break
    
#     return emptiable_node_amount


class Tests(unittest.TestCase):

    def testP1(self):
        pass

def part1(scheme: dict):
    viable_pairs_amount = 0
    for key_A, value_A in scheme.items():
        if value_A['used'] != 0:
            for key_B, value_B in scheme.items():
                if key_A != key_B and value_A['used'] <= value_B['available']:
                    viable_pairs_amount += 1
    
    return viable_pairs_amount


def part2(scheme: dict):
    initial_departure_data_pos = (max(key[0] for key in scheme.keys()), 0)
    for key, value in scheme.items():
        if value['used'] == 0:
            initial_zero_data_pos = key
    firstNode = Node(initial_departure_data_pos, initial_zero_data_pos, 0)
    tree = Tree(scheme, firstNode)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    print(time()-a)

