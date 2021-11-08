from time import time
from itertools import combinations
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]


def part1(scheme: list):
    for couple in combinations(scheme, 2):
        if sum(couple) == 2020:
            return couple[0]*couple[1]


def part2(scheme: list):
    for couple in combinations(scheme, 2):
        if sum(couple) < 2020:
            if 2020 - sum(couple) in scheme and 2020 - sum(couple) not in couple:
                return couple[0]*couple[1]*(2020 - sum(couple))

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = [1721,979,366,299,675,1456]
        self.assertEqual(part1(testInput), 514579)
        self.assertEqual(part2(testInput), 241861950)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

