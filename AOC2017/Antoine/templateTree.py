from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]


class Tree:
    def __init__(self, firstNode):
        # Données du problème
        self.states = {firstNode.state: firstNode.value}
        # Données relatives à l'arbre
        self.bestValue = inf
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
    
    def expandTree(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.value < self.bestValue: # Définir ici la condition de succès
            self.bestValue = currentNode.value
        else:
            for son in currentNode.reachableNodes(self, currentNode.value):
                if son.value < min(self.bestValue, self.states[son.state]):
                    self.states[son.state] = son.value
                    self.openNodes.append(son)


class Node:
    def __init__(self, value):
        self.value = value
        self.state = "" # Définir ici comment qualifier un noeud avec un état unique
    
    def reachableNodes(self, value):
        # Définir ici comment rechercher les prochains noeuds
        yield Node(value)

class Tests(unittest.TestCase):

    def testP1(self):
        pass

def part1(scheme: str):
    tree = Tree(scheme)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp

def part2(scheme: str):
    tree = Tree(scheme)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    print(scheme)
    # p1 = part1(scheme)
    # print(f"Part 1: {p1[0]} in {p1[1]} iterations")
    # p2 = part2(scheme)
    # print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    # print(time()-a)

