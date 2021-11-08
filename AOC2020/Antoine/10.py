from time import time
from collections import deque
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return sorted([int(i.strip()) for i in f.readlines()])

def fractionScheme(scheme: list):
    fractionnedScheme, offset = list(), 0
    for i in range(len(scheme)-1):
        if scheme[i] + 3 == scheme[i+1]:
            fractionnedScheme.append(scheme[offset:i+1])
            offset = i + 1
    fractionnedScheme.append(scheme[offset:])
    return fractionnedScheme

def exploreFractionnedScheme(fractionnedScheme: list):
    maxi, nodesToExplore, paths = max(fractionnedScheme), deque([[min(fractionnedScheme)]]), list()
    while nodesToExplore:
        currentNode = nodesToExplore.popleft()
        for it in range(1,4):
            if currentNode[-1] + it in fractionnedScheme:
                newPath = currentNode + [currentNode[-1]+it]
                if maxi in newPath:
                    paths.append(newPath)
                else:
                    nodesToExplore.append(newPath)
    return len(paths)

            
def part1(scheme: list):
    resDict = {1: 1, 3: 1}
    for ind in range(len(scheme)-1):
        resDict[scheme[ind+1]-scheme[ind]] += 1
    return resDict[1] * resDict[3]

def part2(scheme: list):
    fractionnedScheme = [elem for elem in fractionScheme(scheme) if len(elem) > 1]
    print(scheme,fractionnedScheme)
    res = 1
    for elem in fractionnedScheme:
        res *= exploreFractionnedScheme(elem)
    return res

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2([0]+scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

