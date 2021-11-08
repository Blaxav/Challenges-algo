from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(it) for it in i.strip().split()] for i in f.readlines()]

class Tree:
    def __init__(self, firstNode, int_triangle):
        # Données du problème
        self.states = defaultdict(int)
        self.states[firstNode.state] = firstNode.total
        # Données relatives à l'arbre
        self.bestValue = 0
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
        self.int_triangle = int_triangle
        self.maxRow = [max(row) for row in self.int_triangle]

    
    def expandTree(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.total > self.bestValue and currentNode.row == len(self.int_triangle) - 1: # Définir ici la condition de succès
            self.bestValue = currentNode.total
        else:
            for son in currentNode.reachableNodes(self.int_triangle):
                if self.states[son.state] < son.total:
                    if son.total + sum(self.maxRow[son.row + 1:]) > self.bestValue:
                        self.states[son.state] = son.total
                        self.openNodes.append(son)


class Node:
    def __init__(self, row, column, total):
        self.row = row
        self.column = column
        self.total = total
        self.state = (row, column) # Définir ici comment qualifier un noeud avec un état unique
    
    def reachableNodes(self, int_triangle):
        # Définir ici comment rechercher les prochains noeuds
        for it in range(2):
            if self.row in range(len(int_triangle) - 1):
                yield Node(self.row + 1, self.column + it, self.total + int_triangle[self.row + 1][self.column + it])

def resolution(int_triangle: list):
    firstNode = Node(0, 0, int_triangle[0][0])
    tree = Tree(firstNode, int_triangle)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp

class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    int_triangle = readFile()
    res = resolution(int_triangle)
    print(f"The answer is {res[0]} in {res[1]} iterations")
    print(time()-a)

