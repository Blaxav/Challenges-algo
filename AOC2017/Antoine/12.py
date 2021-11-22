from time import time
import unittest
from collections import deque
from copy import deepcopy
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return {elem.strip().split(' <-> ')[0]:elem.strip().split(' <-> ')[1].split(', ')  for elem in f.readlines()}
            
def part1(scheme: dict, first_node: str):
    explored_nodes, nodes_to_explore = list(), deque([first_node])
    while nodes_to_explore:
        current_node = nodes_to_explore.pop()
        if current_node not in explored_nodes:
            explored_nodes.append(current_node)
        for son_nodes in scheme[current_node]:
            if son_nodes not in explored_nodes:
                nodes_to_explore.append(son_nodes)
        del scheme[current_node]

    return len(explored_nodes)

def part2(scheme: dict):
    groups = list()
    while scheme:
        first_elem = list(scheme.keys())[0]
        groups.append(part1(scheme, first_elem))

    return len(groups)

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(deepcopy(scheme), '0')
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

