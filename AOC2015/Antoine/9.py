from time import time
import unittest
from collections import defaultdict
from itertools import permutations
from math import inf
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def generateDistanceMatrix(scheme: list):
    distanceMatrix = defaultdict(lambda:dict())
    for route in scheme:
        firstSplit = route.split(' = ')
        secondSplit = firstSplit[0].split(' to ')
        distanceMatrix[secondSplit[0]][secondSplit[1]] = int(firstSplit[1])
        distanceMatrix[secondSplit[1]][secondSplit[0]] = int(firstSplit[1])
    return distanceMatrix


def part1(scheme: list):
    distanceMatrix = generateDistanceMatrix(scheme)
    bestValue = inf
    possiblePaths = list(permutations(distanceMatrix.keys()))
    for possiblePath in possiblePaths:
        pathLength = 0
        for it in range(len(possiblePath)-1):
            pathLength += distanceMatrix[possiblePath[it]][possiblePath[it+1]]
        if pathLength > bestValue:
            continue
        if it == len(possiblePath) - 2 and pathLength < bestValue:
            bestValue = pathLength
    return bestValue

def part2(scheme: list):
    distanceMatrix = generateDistanceMatrix(scheme)
    bestValue = 0
    possiblePaths = list(permutations(distanceMatrix.keys()))
    for possiblePath in possiblePaths:
        pathLength = 0
        for it in range(len(possiblePath)-1):
            pathLength += distanceMatrix[possiblePath[it]][possiblePath[it+1]]
        if it == len(possiblePath) - 2 and pathLength > bestValue:
            bestValue = pathLength
    return bestValue

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ['London to Dublin = 464', 'London to Belfast = 518', 'Dublin to Belfast = 141']
        expectedDistanceMatrix = {'London': {'Dublin': 464, 'Belfast': 518}, 'Dublin': {'London': 464, 'Belfast': 141}, 'Belfast': {'London': 518, 'Dublin': 141}}
        self.assertDictEqual(expectedDistanceMatrix, generateDistanceMatrix(testInput))
        self.assertEqual(part1(testInput), 605)
        self.assertEqual(part2(testInput), 982)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

