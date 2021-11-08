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

def generateHapinessMatrix(scheme: list):
    hapinessMatrix = defaultdict(lambda: {})
    for instruction in scheme:
        instruction = instruction.replace('gain ', '').replace('lose ', '-')
        instruction = instruction.split(' ')
        hapinessMatrix[instruction[0]][instruction[9][:-1]] = int(instruction[2]) 
    return hapinessMatrix

def evaluateTable(hapinessMatrix: dict, possibility: tuple):
    val = hapinessMatrix[possibility[0]][possibility[len(possibility)-1]] + hapinessMatrix[possibility[len(possibility)-1]][possibility[0]]
    for it in range(len(possibility)-1):
        val += hapinessMatrix[possibility[it]][possibility[it+1]] + hapinessMatrix[possibility[it+1]][possibility[it]]
    return val


def part1(scheme: list):
    hapinessMatrix = generateHapinessMatrix(scheme)
    guests = list(hapinessMatrix.keys())
    bestValue = -inf
    for possibility in permutations(guests):
        val = evaluateTable(hapinessMatrix, possibility)
        if val > bestValue:
            bestValue = val
    return bestValue

def addMeToTable(hapinessMatrix: dict, myName: str):
    for elem in hapinessMatrix:
        hapinessMatrix[elem][myName] = 0
    hapinessMatrix[myName] = {k:0 for k in hapinessMatrix}
    return hapinessMatrix

def part2(scheme: list):
    hapinessMatrix = addMeToTable(generateHapinessMatrix(scheme), 'Antoine')
    print(hapinessMatrix)
    guests = list(hapinessMatrix.keys())
    bestValue = -inf
    for possibility in permutations(guests):
        val = evaluateTable(hapinessMatrix, possibility)
        if val > bestValue:
            bestValue = val
    return bestValue

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ['Alice would gain 54 happiness units by sitting next to Bob.','Alice would lose 79 happiness units by sitting next to Carol.','Alice would lose 2 happiness units by sitting next to David.','Bob would gain 83 happiness units by sitting next to Alice.','Bob would lose 7 happiness units by sitting next to Carol.','Bob would lose 63 happiness units by sitting next to David.','Carol would lose 62 happiness units by sitting next to Alice.','Carol would gain 60 happiness units by sitting next to Bob.','Carol would gain 55 happiness units by sitting next to David.','David would gain 46 happiness units by sitting next to Alice.','David would lose 7 happiness units by sitting next to Bob.','David would gain 41 happiness units by sitting next to Carol.']
        expectedHapinessMatrix = {'Alice': {'Bob': 54, 'Carol': -79, 'David': -2}, 'Bob': {'Alice': 83, 'Carol': -7, 'David': -63}, 'Carol': {'Alice': -62, 'Bob': 60, 'David': 55}, 'David': {'Alice': 46, 'Bob': -7, 'Carol': 41}}
        self.assertDictEqual(expectedHapinessMatrix, generateHapinessMatrix(testInput))
        self.assertEqual(part1(testInput), 330)

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

