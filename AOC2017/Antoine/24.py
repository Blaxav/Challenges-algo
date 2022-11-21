from time import time
from math import inf
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [tuple(int(port) for port in i.strip().split('/')) for i in f.readlines()]

def identify_connections(scheme: list):
    connections = defaultdict(set)
    for component in scheme:
        for port in component:
            for connecting_component in scheme:
                if component != connecting_component:
                    if port in connecting_component:
                        connections[port].add(connecting_component)
    
    return connections

class Tree:
    def __init__(self, scheme, connections):
        self.connections = connections
        self.strongest_bridge = 0
        self.longest_bridge_length = 0
        self.longest_bridge_strengh = 0
        self.openNodes = deque([Node([component], 1, 1) for component in scheme if component[0] == 0])
    
    def expandTree(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        if currentNode.value > self.strongest_bridge: # Définir ici la condition de succès
            self.strongest_bridge = currentNode.value
        if len(currentNode.components) > self.longest_bridge_length or (len(currentNode.components) == self.longest_bridge_length and currentNode.value > self.longest_bridge_strengh):
            self.longest_bridge_length = len(currentNode.components)
            self.longest_bridge_strengh = currentNode.value
        for son in currentNode.reachableNodes(self.connections):
            self.openNodes.append(son)


class Node:
    def __init__(self, components, not_connected_port_index, length):
        self.components = components
        self.value = sum(component[0] + component[1] for component in self.components)
        self.not_connected_port = self.components[-1][not_connected_port_index]
        self.length = length
    
    def reachableNodes(self, connections):
        for connectable_component in connections[self.not_connected_port]:
            if connectable_component not in self.components:
                yield Node(self.components + [connectable_component], ~connectable_component.index(self.not_connected_port), self.length + 1)

class Tests(unittest.TestCase):

    def testP1(self):
        pass

def part1(scheme: list, connections: dict):
    tree = Tree(scheme, connections)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.strongest_bridge, tree.longest_bridge_strengh, comp
        
if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    connections = identify_connections(scheme)
    p1 = part1(scheme, connections)
    print(f"Part 1: {p1[0]} and part 2 : {p1[1]} in {p1[2]} iterations")
    print(time()-a)

