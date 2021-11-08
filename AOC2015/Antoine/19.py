from time import time
import unittest
from collections import defaultdict, deque
import re
from math import inf
from sys import getsizeof
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines() if i.strip()]

def generateReactionTable(scheme: list):
    reactionTable = defaultdict(lambda: [])
    for reaction in scheme:
        reaction = reaction.split()
        reactionTable[reaction[0]].append(reaction[2])
    return reactionTable

            
def part1(reactions: list, molecule: str):
    reactionTable = generateReactionTable(reactions)
    possibilities = []
    for reactive, products in reactionTable.items():
        indexes = [m.start() for m in re.finditer(reactive, molecule)]
        for index in indexes:
            for product in products:
                possibility = molecule[:index] + product + molecule[index+len(reactive):]
                if possibility not in possibilities:
                    possibilities.append(possibility)
    return possibilities

def generateInvertReactionTable(scheme: list):
    reactionTable = dict()
    for reaction in scheme:
        reaction = reaction.split()
        reactionTable[reaction[2]] = reaction[0]
    return reactionTable

def inverseReactions(reactions: dict, molecule: str):
    possibilities = []
    for reactive, products in reactions.items():
        indexes = [m.start() for m in re.finditer(reactive, molecule)]
        for index in indexes:
            for product in products:
                possibility = molecule[:index] + product + molecule[index+len(reactive):]
                if possibility not in possibilities:
                    yield possibility

class Node:
    def __init__(self, string, it):
        self.molecule = string
        self.it = it
    
    def generateSons(self, reactions: dict):
        for reactive, product in reactions.items():
            indexes = [m.start() for m in re.finditer(reactive, self.molecule)]
            for index in indexes:
                yield self.molecule[:index] + product + self.molecule[index+len(reactive):]

def part2(reactions: list, molecule: str):
    reactionTable = generateInvertReactionTable(reactions)
    finalMolecules = [k for k,v in reactionTable.items() if v == 'e']
    for elem in finalMolecules:
        del reactionTable[elem]
    bestValue = inf
    openNodes = deque([])
    openNodes.append(Node(molecule, 0))
    comp = 0
    states = defaultdict(lambda: inf)
    while openNodes:
        newMolecule = openNodes.pop()
        if not comp % 100_000:
            print(bestValue, len(openNodes), len(newMolecule.molecule))
        for son in newMolecule.generateSons(reactionTable):
            if newMolecule.it + 1 < states[son]: 
                states[son] = newMolecule.it + 1
                comp += 1
                if son in finalMolecules and newMolecule.it + 2 < bestValue:
                    bestValue = newMolecule.it + 2
                else:
                    if newMolecule.it + 1 < bestValue:
                        openNodes.append(Node(son, newMolecule.it + 1))
    return bestValue

class Tests(unittest.TestCase):

    def testP1(self):
        testInput, mol = ['H => HO', 'H => OH', 'O => HH', 'e => H', 'e => O'], 'HOH'
        # self.assertEqual(part1(testInput, mol), 4)
        self.assertEqual(part2(testInput, mol), 3)
        testInput, mol = ['H => HO', 'H => OH', 'O => HH', 'e => H', 'e => O'], 'HOHOHO'
        self.assertEqual(part2(testInput, mol), 6)

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    reactions, molecule = scheme[:-1], scheme[-1]
    p1 = part1(reactions, molecule)
    print(f"Part 1: {len(p1)}")
    p2 = part2(reactions, molecule)
    print(f"Part 2: {len(p2)}")
    print(time()-a)

