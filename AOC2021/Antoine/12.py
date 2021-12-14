from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().split('-') for i in f.readlines()]

def create_graph(scheme: list):
    graph = defaultdict(list)
    for elem in scheme:
        graph[elem[0]].append(elem[1])
        graph[elem[1]].append(elem[0])
    
    return graph

class Tree:
    def __init__(self, firstNode, graph, part):
        # Données du problème
        self.paths = 0
        self.part = part
        # Données relatives à l'arbre
        self.bestValue = inf
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
        self.graph = graph
    
    def expandTree(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.cave == 'end':
            self.paths += 1
            if currentNode.value < self.bestValue: # Définir ici la condition de succès
                self.bestValue = currentNode.value
        else:
            for son in currentNode.reachableNodes(self.graph, self.part):
                self.openNodes.append(son)


class Node:
    def __init__(self, cave, path):
        self.cave = cave
        self.value = path.count('-')
        self.path = path # Définir ici comment qualifier un noeud avec un état unique
    
    def reachableNodes(self, graph, part):
        # Définir ici comment rechercher les prochains noeuds
        for reachable_cave in graph[self.cave]:
            if part == 1:
                if reachable_cave.upper() == reachable_cave or reachable_cave not in self.path:
                    yield Node(reachable_cave, f'{self.path}-{reachable_cave}')
            if part == 2:
                explored_small_caves = [elem for elem in self.path.split('-') if elem.lower() == elem and len(elem) == 2]
                if reachable_cave.upper() == reachable_cave or reachable_cave not in self.path:
                    yield Node(reachable_cave, f'{self.path}-{reachable_cave}')
                elif len(explored_small_caves) == len(set(explored_small_caves)) and len(reachable_cave) == 2:
                    yield Node(reachable_cave, f'{self.path}-{reachable_cave}')

class Tests(unittest.TestCase):

    def testP1(self):
        pass

def part1(scheme: str):
    graph = create_graph(scheme)
    firstNode = Node('start', 'start')
    tree = Tree(firstNode, graph, 1)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.paths, comp

def part2(scheme: str):
    graph = create_graph(scheme)
    firstNode = Node('start', 'start')
    tree = Tree(firstNode, graph, 2)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.paths, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1[0]} in {p1[1]} iterations")
    p2 = part2(scheme)
    print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    # print(time()-a)

