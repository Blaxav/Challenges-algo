from time import time
from math import inf
from collections import deque, defaultdict
import unittest
import hashlib
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def md5(string: str):
    return hashlib.md5(string.encode('utf-8')).hexdigest()[:4]

class Tree:
    def __init__(self, firstNode):
        # Données relatives à l'arbre
        self.bestValueP1 = inf
        self.bestValueP2 = 0
        self.bestPath = None
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
    
    def expandTreeP1(self):
        currentNode = self.openNodes.popleft() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.value < self.bestValueP1 and currentNode.position == 15: # Définir ici la condition de succès
            self.bestValueP1 = currentNode.value
            self.bestPath = currentNode.state
        else:
            for son in currentNode.reachableNodes():
                if son.value < self.bestValueP1:
                    self.openNodes.append(son)
    
    def expandTreeP2(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.position == 15: # Définir ici la condition de succès:
            if currentNode.value > self.bestValueP2:
                self.bestValueP2 = currentNode.value
                self.bestPath = currentNode.state
        else:
            for son in currentNode.reachableNodes():
                self.openNodes.append(son)


class Node:
    def __init__(self, state, value, position):
        self.state = state # Définir ici comment qualifier un noeud avec un état unique
        self.value = value
        self.position = position
    
    def reachableNodes(self):
        # Définir ici comment rechercher les prochains noeuds
        for count, char in enumerate(md5(self.state)):
            if char in ["b", "c", "d", "e", "f"]:
                if count == 0 and self.position > 3:
                    yield Node(self.state + "U", self.value + 1, self.position - 4)
                if count == 1 and self.position < 12:
                    yield Node(self.state + "D", self.value + 1, self.position + 4)
                if count == 2 and self.position % 4:
                    yield Node(self.state + "L", self.value + 1, self.position - 1)
                if count == 3 and (self.position + 1) % 4:
                    yield Node(self.state + "R", self.value + 1, self.position + 1)

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1("ihgpwlah")[0], "DDRRRD")
        self.assertEqual(part1("kglvqrro")[0], "DDUDRLRRUDRD")
        self.assertEqual(part1("ulqzkmiv")[0], "DRURDRUDDLLDLUURRDULRLDUUDDDRR")
    
    def testP2(self):
        self.assertEqual(part2("ihgpwlah")[1], 370)
        self.assertEqual(part2("kglvqrro")[1], 492)
        self.assertEqual(part2("ulqzkmiv")[1], 830)

def part1(scheme: str):
    firstNode = Node(scheme, 0, 0)
    tree = Tree(firstNode)
    comp = 0
    while tree.openNodes:
        tree.expandTreeP1()
        comp += 1
    return tree.bestPath[len(scheme):], tree.bestValueP1, comp

def part2(scheme: str):
    firstNode = Node(scheme, 0, 0)
    tree = Tree(firstNode)
    comp = 0
    while tree.openNodes:
        tree.expandTreeP2()
        comp += 1
    return tree.bestPath[len(scheme):], tree.bestValueP2, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: The shortest path is {p1[0]} of length {p1[1]} in {p1[2]} iterations")
    p2 = part2(scheme)
    print(f"Part 2: The longest path is {p2[0]} of length {p2[1]} in {p2[2]} iterations")
    # print(time()-a)

