from time import time
import unittest
from itertools import combinations
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]
            
def part1(scheme: list, storage: int):
    comp = 0
    for k in range(1, len(scheme)+1):
        gen = (1 for a in combinations(scheme, k) if sum(a) == storage)
        comp += sum(gen)
    return comp

def part2(scheme: list, storage: int):
    comp = 0
    for k in range(1, len(scheme)+1):
        gen = (1 for a in combinations(scheme, k) if sum(a) == storage)
        comp += sum(gen)
        if comp > 0:
            return comp
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = [5,5,10,15,20]
        self.assertEqual(part1(testInput, 25), 4)
        self.assertEqual(part2(testInput, 25), 3)



if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 150)
    print(f"Part 1: {p1}")
    p2 = part2(scheme, 150)
    print(f"Part 2: {p2}")
    print(time()-a)

