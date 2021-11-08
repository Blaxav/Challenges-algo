from time import time
import unittest
from math import prod
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def generateQualityTable(scheme: list):
    qualityTable = dict()
    for num, elem in enumerate(scheme):
        elem = elem.split()
        qualityTable[num] = (int(elem[2][:-1]), int(elem[4][:-1]), int(elem[6][:-1]), int(elem[8][:-1]), int(elem[10]))#{elem[1]: int(elem[2][:-1]), elem[3]: int(elem[4][:-1]), elem[5]: int(elem[6][:-1]), elem[7]: int(elem[8][:-1])}
    return qualityTable

def part1(scheme: list):
    genComposition = ((a,b,c,d) for a in range(101) for b in range(101) for c in range(101) for d in range(101) if a+b+c+d == 100)
    qualityTable = generateQualityTable(scheme)
    bestValue = 0
    for composition in genComposition:
        recipe = tuple(tuple(qualityTable[itQuant][itIng]*composition[itQuant] for itIng in range(4)) for itQuant in range(4))
        val = prod(tuple(max(sum((recipe[itIng][itQuant] for itIng in range(4))),0) for itQuant in range(4)))
        if val > bestValue:
            bestValue = val
    return bestValue

def part2(scheme: list):
    genComposition = ((a,b,c,d) for a in range(101) for b in range(101) for c in range(101) for d in range(101) if a+b+c+d == 100)
    qualityTable = generateQualityTable(scheme)
    bestValue = 0
    for composition in genComposition:
        recipe = tuple(tuple(qualityTable[itQuant][itIng]*composition[itQuant] for itIng in range(4)) for itQuant in range(4))
        val = prod(tuple(max(sum((recipe[itIng][itQuant] for itIng in range(4))),0) for itQuant in range(4)))
        calories = sum(qualityTable[it][4]*composition[it] for it in range(4))
        if val > bestValue and calories == 500:
            bestValue = val
    return bestValue

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8' ,'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']
        # expectedQualityTable = {'Butterscotch': {'capacity': -1, 'durability': -2, 'flavor': 6, 'texture': 3}, 'Cinnamon': {'capacity': 2, 'durability': 3, 'flavor': -2, 'texture': -1}}
        expectedQualityTable = {0: (-1, -2, 6, 3), 1: (2, 3, -2, -1)}
        self.assertDictEqual(expectedQualityTable, generateQualityTable(testInput))

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

