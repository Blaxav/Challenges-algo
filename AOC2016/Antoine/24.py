from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        # return [it for i in f.readlines() for it in i.strip()]
        return [i.strip() for i in f.readlines()]

def extract_problem_data(scheme):
    linear_scheme = [it for i in scheme for it in i]
    key_amount = max(int(it) for it in linear_scheme if it.isdigit()) + 1
    return len(scheme), len(scheme[0]), key_amount, linear_scheme

def get_neighbours(pos: int, width: int):
    neighbours_delta = {'left': -1, 'right': 1, 'up': -width, 'down': width}
    return {direction: scheme[pos + delta] for direction, delta in neighbours_delta.items() if pos + delta in range(len(scheme)) and scheme[pos + delta] != "#"}

def is_cross(pos: int, width: int, scheme: list):
    return len(get_neighbours(pos, width)) > 2 or scheme[pos].isdigit()

def is_cul_de_sac(pos: int, width: int):
    return len(get_neighbours(pos, width)) < 2


def generate_crosses_mapping(scheme: list, key_amount: int, width: int):
    count, dict_crosses = key_amount, dict()
    for pos, elem in enumerate(scheme):
        if elem.isdigit():
            dict_crosses[pos] = int(elem)
        elif elem == "." and is_cross(pos, width, scheme):
            dict_crosses[pos] = count
            count += 1
    
    return dict_crosses

def generate_neighbours_mapping(crosses_mapping: dict, width: int, scheme: list):
    neighbours_mapping = defaultdict(dict)
    neighbours_delta, opposite_direction = {'left': -1, 'right': 1, 'up': -width, 'down': width}, {'left': 'right', 'right': 'left', 'up': 'down', 'down': 'up'}
    for cross_position, cross in crosses_mapping.items():
        explored_path = dict()
        for direction in get_neighbours(cross_position, width):
            explored_pos, next_direction, steps, can_continue = cross_position, direction, 0, True
            while can_continue:
                explored_pos += neighbours_delta[next_direction]
                steps += 1
                if is_cross(explored_pos, width, scheme):
                    explored_path[direction] = (crosses_mapping[explored_pos], steps)
                    can_continue = False
                elif is_cul_de_sac(explored_pos, width):
                    can_continue = False
                else:
                    next_direction = [neighbour_direction for neighbour_direction, neighbour_symbol in get_neighbours(explored_pos, width).items() if (neighbour_symbol == "." or neighbour_symbol.isdigit()) and neighbour_direction != opposite_direction[next_direction]][0]
        neighbours_mapping[cross] = explored_path

    return neighbours_mapping


class Tree:
    def __init__(self, crosses_mapping, neighbours_mapping, firstNode, key_amount):
        # Données du problème
        self.states = defaultdict(lambda: inf)
        self.states[firstNode.state] = firstNode.value
        # Données relatives à l'arbre
        self.bestValue = inf
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
        self.neighbours_mapping = neighbours_mapping
        self.crosses_mapping = crosses_mapping
        self.key_amount = key_amount
        self.part2 = part2
    
    def expandTree(self):
        currentNode = self.openNodes.popleft() # .pop() -> profondeur, .popleft() -> largeur
        if len(currentNode.keys) == self.key_amount and currentNode.value < self.bestValue: # Définir ici la condition de succès
            self.bestValue = currentNode.value
        else:
            for son in currentNode.reachableNodes(self.neighbours_mapping, self.key_amount):
                if son.value < min(self.bestValue, self.states[son.state]):
                    self.states[son.state] = son.value
                    self.openNodes.append(son)
    
    def expandTree_p2(self):
        currentNode = self.openNodes.popleft() # .pop() -> profondeur, .popleft() -> largeur
        if len(currentNode.keys) == self.key_amount + 1 and currentNode.keys.endswith('0') and currentNode.value < self.bestValue: # Définir ici la condition de succès
            self.bestValue = currentNode.value
        else:
            for son in currentNode.reachableNodes_p2(self.neighbours_mapping, self.key_amount):
                if son.value < min(self.bestValue, self.states[son.state]):
                    self.states[son.state] = son.value
                    self.openNodes.append(son)


class Node:
    def __init__(self, keys, cross_id, value):
        self.keys = keys
        self.cross_id = cross_id
        self.value = value
        self.state = ("".join(sorted(keys)), cross_id) # Définir ici comment qualifier un noeud avec un état unique
    
    def reachableNodes(self, neighbours_mapping, key_amount):
        # Définir ici comment rechercher les prochains noeuds
        for neighbour in neighbours_mapping[self.cross_id].values():
            new_key = str(neighbour[0]) if neighbour[0] < key_amount and str(neighbour[0]) not in self.keys else ""
            yield Node(self.keys + new_key, neighbour[0], self.value + neighbour[1])
    
    def reachableNodes_p2(self, neighbours_mapping, key_amount):
        # Définir ici comment rechercher les prochains noeuds
        for neighbour in neighbours_mapping[self.cross_id].values():
            new_key = str(neighbour[0]) if neighbour[0] < key_amount and ( str(neighbour[0]) not in self.keys or ( neighbour[0] == 0 and len(self.keys) == key_amount ) ) else ""
            yield Node(self.keys + new_key, neighbour[0], self.value + neighbour[1])

class Tests(unittest.TestCase):

    def testP1(self):
        pass

def part1(neighbours_mapping: dict, key_amount: int):
    firstNode = Node("0", 0, 0)
    tree = Tree(crosses_mapping, neighbours_mapping, firstNode, key_amount)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp

def part2(neighbours_mapping: dict, key_amount: int):
    firstNode = Node("0", 0, 0)
    tree = Tree(crosses_mapping, neighbours_mapping, firstNode, key_amount)
    comp = 0
    while tree.openNodes:
        tree.expandTree_p2()
        comp += 1
    return tree.bestValue, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    length, width, key_amount, scheme = extract_problem_data(scheme)
    crosses_mapping = generate_crosses_mapping(scheme, key_amount, width)
    neighbours_mapping = generate_neighbours_mapping(crosses_mapping, width, scheme)
    p1 = part1(neighbours_mapping, key_amount)
    print(f"Part 1: {p1[0]} in {p1[1]} iterations")
    p2 = part2(neighbours_mapping, key_amount)
    print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    print(time()-a)

