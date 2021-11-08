from time import time
import unittest
from collections import defaultdict
from copy import deepcopy
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def generateLightMap(scheme: list):
    lightMap = defaultdict(int)
    for row, line in enumerate(scheme):
        for col, char in enumerate(line):
            if char == '#':
                lightMap[(row,col)] = 1
            else:
                lightMap[(row,col)] = 0
    return lightMap

def getAmountOfAdjacentLights(coord: tuple, lightMap: dict):
    xref, yref = coord
    return sum(lightMap[(x,y)] for x in range(xref-1, xref+2) for y in range(yref-1, yref+2) if (x,y) != (xref,yref))

def oneStep(lightMap: dict):
    newLightMap = defaultdict(int)
    for case, val in deepcopy(lightMap).items():
        if val == 1:
            newLightMap[case] = 1 if getAmountOfAdjacentLights(case, lightMap) in [2,3] else 0
        else:
            newLightMap[case] = 1 if getAmountOfAdjacentLights(case, lightMap) == 3 else 0
    return newLightMap
            
def part1(scheme: list, iterations: int):
    lightMap = generateLightMap(scheme)
    for it in range(iterations):
        lightMap = oneStep(lightMap)
    return sum(lightMap.values())

def oneStepTwo(lightMap: dict):
    newLightMap = defaultdict(int)
    for case, val in deepcopy(lightMap).items():
        if case in [(0,0), (0,99), (99,0), (99,99)]:
            newLightMap[case] = 1
        elif val == 1:
            newLightMap[case] = 1 if getAmountOfAdjacentLights(case, lightMap) in [2,3] else 0
        else:
            newLightMap[case] = 1 if getAmountOfAdjacentLights(case, lightMap) == 3 else 0
    return newLightMap

def part2(scheme: list, iterations: int):
    lightMap = generateLightMap(scheme)
    lightMap[(0,0)], lightMap[(0,99)], lightMap[(99,0)], lightMap[(99,99)] = 1,1,1,1
    for it in range(iterations):
        lightMap = oneStepTwo(lightMap)
    return sum(lightMap.values())

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ['.#.#.#','...##.','#....#','..#...','#.#..#','####..']
        res = [15, 11, 8, 4, 4]
        for it in range(5):
            self.assertEqual(part1(testInput, it), res[it])


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 100)
    print(f"Part 1: {p1}")
    p2 = part2(scheme, 100)
    print(f"Part 2: {p2}")
    print(time()-a)

