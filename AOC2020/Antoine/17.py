from time import time
from copy import deepcopy
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def parseScheme(scheme:list):
    cubes = list()
    for itLine, line in enumerate(scheme):
        for itColumn, char in enumerate(line):
            if char == '#':
                cubes.append((itLine, itColumn, 0))
    
    return cubes

def getNeighbours(cubes: list, x: int, y: int, z: int):
    return len([(x+x1,y+y1,z+z1) for x1 in range(-1, 2) for y1 in range(-1, 2) for z1 in range(-1, 2) if (x+x1, y+y1, z+z1) in cubes and (x1, y1, z1) != (0, 0, 0)])

def getRangeOfExploration(cubes: list):
    xList, yList, zList = [elem[0] for elem in cubes], [elem[1] for elem in cubes], [elem[2] for elem in cubes]
    return min(xList) - 1, max(xList) + 1, min(yList) - 1, max(yList) + 1, min(zList) - 1, max(zList) + 1

def expandScheme(cubes: list):
    xMin, xMax, yMin, yMax, zMin, zMax = getRangeOfExploration(cubes)
    newCubes = []
    newCubes.extend(cubes)
    for x in range(xMin, xMax+1):
        for y in range(yMin, yMax+1):
            for z in range(zMin, zMax+1):
                if (x, y, z) in cubes:
                    if getNeighbours(cubes, x, y, z) not in [2, 3]:
                        newCubes.remove((x, y, z))
                else:
                    if getNeighbours(cubes, x, y, z) == 3:
                        newCubes.append((x, y, z))
    
    return newCubes

def parseSchemeP2(scheme:list):
    cubes = list()
    for itLine, line in enumerate(scheme):
        for itColumn, char in enumerate(line):
            if char == '#':
                cubes.append((itLine, itColumn, 0, 0))
    
    return cubes

def getNeighboursP2(cubes: list, x: int, y: int, z: int, w: int):
    return len([(x+x1,y+y1,z+z1, w+w1) for x1 in range(-1, 2) for y1 in range(-1, 2) for z1 in range(-1, 2) for w1 in range(-1, 2) if (x+x1, y+y1, z+z1, w+w1) in cubes and (x1, y1, z1, w1) != (0, 0, 0, 0)])

def getRangeOfExplorationP2(cubes: list):
    xList, yList, zList, wList = [elem[0] for elem in cubes], [elem[1] for elem in cubes], [elem[2] for elem in cubes], [elem[3] for elem in cubes]
    return min(xList) - 1, max(xList) + 1, min(yList) - 1, max(yList) + 1, min(zList) - 1, max(zList) + 1, min(wList) - 1, max(wList) + 1

def expandSchemeP2(cubes: list):
    xMin, xMax, yMin, yMax, zMin, zMax, wMin, wMax = getRangeOfExplorationP2(cubes)
    newCubes = []
    newCubes.extend(cubes)
    for x in range(xMin, xMax+1):
        for y in range(yMin, yMax+1):
            for z in range(zMin, zMax+1):
                for w in range(wMin, wMax+1):
                    if (x, y, z, w) in cubes:
                        if getNeighboursP2(cubes, x, y, z, w) not in [2, 3]:
                            newCubes.remove((x, y, z, w))
                    else:
                        if getNeighboursP2(cubes, x, y, z, w) == 3:
                            newCubes.append((x, y, z, w))
    
    return newCubes
            
def part1(scheme: list, iterations: int):
    cubes = parseScheme(scheme)
    for it in range(iterations):
        cubes = expandScheme(cubes)
    return len(cubes)

def part2(scheme: list, iterations: int):
    cubes = parseSchemeP2(scheme)
    for it in range(iterations):
        cubes = expandSchemeP2(cubes)
    return len(cubes)

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 6)
    print(f"Part 1: {p1}")
    p2 = part2(scheme, 6)
    print(f"Part 2: {p2}")
    print(time()-a)

