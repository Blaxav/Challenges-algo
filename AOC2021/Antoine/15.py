from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(it) for i in f.readlines() for it in i.strip()]

def get_neighbours_position(position: int, scheme: list):
    scheme_width = int(sqrt(len(scheme)))
    if position % scheme_width == 0:
        return (position + delta for delta in (-scheme_width, 1, scheme_width) if position + delta in range(len(scheme)))
    elif (position + 1) % scheme_width == 0:
        return (position + delta for delta in (-1, scheme_width) if position + delta in range(len(scheme)))
    elif len(scheme) - scheme_width <= position < len(scheme):
        return (position + delta for delta in (-scheme_width, 1) if position + delta in range(len(scheme)))
    else:
        return (position + delta for delta in (-scheme_width, -1, 1, scheme_width) if position + delta in range(len(scheme)))

def generate_map(scheme: list):
    scheme_width = int(sqrt(len(scheme)))
    new_scheme = list()
    for y in range(5):
        for it in range(scheme_width):
            row = scheme[scheme_width * it : scheme_width * (it + 1)]
            for x in range(5):
                new_scheme += [(elem + x + y if elem + x + y < 10 else elem + x + y - 9) for elem in row]
    
    return new_scheme

class Tree:
    def __init__(self, firstNode, scheme):
        # Données du problème
        self.states = defaultdict(lambda: inf)
        self.states[firstNode.position] = 0
        # Données relatives à l'arbre
        self.bestValue = sum(scheme)
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
        self.scheme = scheme
    
    def expandTree(self):
        currentNode = self.openNodes.popleft() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.position == len(self.scheme) - 1 and self.states[currentNode.position] < self.bestValue: # Définir ici la condition de succès
            self.bestValue = self.states[currentNode.position]
        else:
            for son in currentNode.reachableNodes(self.scheme):
                if self.states[currentNode.position] + scheme[son.position] < min(self.bestValue, self.states[son.position]):
                    self.states[son.position] = self.states[currentNode.position] + scheme[son.position]
                    self.openNodes.append(son)


class Node:
    def __init__(self, position):
        self.position = position
    
    def reachableNodes(self, scheme):
        # Définir ici comment rechercher les prochains noeuds
        for neighbour_position in get_neighbours_position(self.position, scheme):
            yield Node(neighbour_position)

class Tests(unittest.TestCase):

    def testP1(self):
        pass

def part1(scheme: list):
    tree = Tree(Node(0), scheme)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1[0]} in {p1[1]} iterations")
    scheme = generate_map(scheme)
    p2 = part1(scheme)
    print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    print(time()-a)

