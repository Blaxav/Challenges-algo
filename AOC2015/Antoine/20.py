from time import time
import unittest
from itertools import cycle
import numpy as np
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return int(f.readline().strip())

def divisorsSum(num: int):
    return sum(i for i in range(1, num+1) if num % i == 0)

def yieldGenerators(num: int):
    for i in range(1, num):
        gen = (int(k == i) for k in range(1, i+1))
        yield cycle(gen)


def part1(scheme: int):
    goal = int(scheme/10)
    supremum = int(goal/2)
    houses = np.zeros(supremum)
    for it in range(1, supremum):
        houses[it::it] += it
    for num, elem in enumerate(houses, 0):
        if elem >= goal:
            return num

def part2(scheme: list):
    goal = int(scheme/10)
    supremum = int(goal/2)
    houses = np.zeros(supremum)
    for it in range(1, supremum):
        houses[it:50*it+1:it] += 1.1*it
    for num, elem in enumerate(houses, 0):
        if elem >= goal:
            return num

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

