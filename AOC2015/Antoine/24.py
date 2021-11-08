from time import time
import unittest
from itertools import combinations
from math import prod
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]

            
def part1(scheme: list):
    weight = int(sum(scheme)/3)
    possibilities = []
    it = 1
    while not possibilities:
        possibilities = [prod(a) for a in combinations(scheme, it) if sum(a) == weight]
        it += 1
    return min(possibilities)

def part2(scheme: list):
    weight = int(sum(scheme)/4)
    possibilities = []
    it = 1
    while not possibilities:
        possibilities = [prod(a) for a in combinations(scheme, it) if sum(a) == weight]
        it += 1
    return min(possibilities)

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

