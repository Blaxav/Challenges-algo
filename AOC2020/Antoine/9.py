from time import time
from itertools import combinations
from collections import deque
import unittest
a = time()


def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]


def part1(scheme: list):
    ind = 0
    while ind < len(scheme)-25:
        if scheme[ind+25] not in [sum(a) for a in combinations(scheme[ind:ind+25], 2)]:
            return scheme[ind+25]
        else:
            ind += 1
        

def part2(scheme: list):
    res = part1(scheme)
    startInd = 0
    while startInd < len(scheme)-25:
        partialSum, partialInd = 0, startInd
        resList = list()
        while partialSum < res:
            resList.append(scheme[partialInd])
            partialSum += scheme[partialInd]
            if partialSum == res:
                return min(resList) + max(resList)
            partialInd += 1
        startInd += 1


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
