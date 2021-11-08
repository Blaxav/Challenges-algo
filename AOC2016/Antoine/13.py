from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return int(f.readline())

def wallOrPath(x: int, y: int, inputNumber: int):
    return bin(x*x + 3*x + 2*x*y + y + y*y + inputNumber).count("1") % 2

class Tree:
    def __init__(self, firstNode, inputNumber: int, arrival: tuple, limit: int):
        # Données du problème
        self.states = {firstNode.state: firstNode.value}
        self.inputNumber = inputNumber
        self.arrival = arrival
        self.limit = limit
        # Données relatives à l'arbre
        self.bestValue = 0
        self.openNodes = deque([firstNode])
    
    def expandTree(self):
        currentNode = self.openNodes.popleft() # .pop() -> profondeur, .popleft() -> largeur
        if (currentNode.x, currentNode.y) == self.arrival:
            self.bestValue = currentNode.value
            self.openNodes.clear()
        else:
            for son in currentNode.reachableNodes(self.inputNumber):
                if son.state not in self.states or son.value < self.states[son.state]:
                    self.states[son.state] = son.value
                    self.openNodes.append(son)
    
    def exploreTree(self):
        currentNode = self.openNodes.popleft() # .pop() -> profondeur, .popleft() -> largeur
        for son in currentNode.explorableNodes(self.inputNumber, self.limit):
            if son.state not in self.states or son.value < self.states[son.state]:
                self.states[son.state] = son.value
                self.openNodes.append(son)


class Node:
    def __init__(self, x: int, y: int, value: int):
        self.x = x
        self.y = y
        self.value = value
        self.state = (x, y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def reachableNodes(self, inputNumber):
        moves = (-1, 1)
        for move in moves:
            new_x = self.x + move
            if new_x >= 0 and not wallOrPath(new_x, self.y, inputNumber):
                yield Node(new_x, self.y, self.value + 1)
        for move in moves:
            new_y = self.y + move
            if new_y >= 0 and not wallOrPath(self.x, new_y, inputNumber):
                yield Node(self.x, new_y, self.value + 1)
    
    def explorableNodes(self, inputNumber, limit):
        moves = (-1, 1)
        if self.value < limit:
            for move in moves:
                new_x = self.x + move
                if new_x >= 0 and not wallOrPath(new_x, self.y, inputNumber):
                    yield Node(new_x, self.y, self.value + 1)
            for move in moves:
                new_y = self.y + move
                if new_y >= 0 and not wallOrPath(self.x, new_y, inputNumber):
                    yield Node(self.x, new_y, self.value + 1)

class Tests(unittest.TestCase):

    def testP1(self):
        inputNumber = 10
        self.assertEqual(wallOrPath(5, 2, inputNumber), 1)
        self.assertEqual(wallOrPath(0, 0, inputNumber), 0)
        self.assertEqual(wallOrPath(1, 5, inputNumber), 0)
        self.assertEqual(wallOrPath(1, 1, inputNumber), 0)
        arrival = (7, 4)
        self.assertEqual(part1(arrival)[0], 11)

def part1(arrival: tuple):
    inputNumber = readFile()
    tree = Tree(Node(1, 1, 0), inputNumber, arrival, inf)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp

def part2(limit: int):
    inputNumber = readFile()
    tree = Tree(Node(1, 1, 0), inputNumber, (0, 0), limit)
    comp = 0
    while tree.openNodes:
        tree.exploreTree()
        comp += 1
    return len(tree.states), comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    arrival = (31, 39)
    p1 = part1(arrival)
    print(f"Part 1: {p1[0]} in {p1[1]} iterations")
    p2 = part2(50)
    print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    print(time()-a)
