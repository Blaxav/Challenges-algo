from time import time
import re
from itertools import cycle
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def parseScheme(scheme: list):
    cycles = dict() 
    for instruction in scheme:
        discNumber, positionsAmount, initialPosition = [int(a) for a in re.split("Disc #| has | positions; at time=0, it is at position |\.", instruction) if a]
        cycle = [str(a) for a in range(positionsAmount)][initialPosition:] + [str(a) for a in range(positionsAmount)][:initialPosition]
        positionToLetTheBallPass = cycle[(cycle.index('0') - discNumber) % positionsAmount]
        cycles[discNumber] = (cycle, positionToLetTheBallPass)
    return cycles


def part1(scheme: list):
    cycles = parseScheme(scheme)
    combinations, goal = zip(*[cycle(a[0]) for a in cycles.values()]), tuple([a[1] for a in cycles.values()])
    for num, elem in enumerate(combinations):
        if elem == goal:
            return num

def part2(scheme: list):
    scheme.append(f"Disc #{len(scheme)+1} has 11 positions; at time=0, it is at position 0.")
    return part1(scheme)

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ["Disc #1 has 5 positions; at time=0, it is at position 4.", "Disc #2 has 2 positions; at time=0, it is at position 1."]
        self.assertEqual(parseScheme(testInput), {1:(['4','0','1','2','3'], '4'), 2:(['1','0'], '0')})
        self.assertEqual(part1(testInput), 5)

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

