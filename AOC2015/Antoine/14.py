from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def generateSpeedTable(scheme: list):
    speedTable = dict()
    for elem in scheme:
        elem = elem.split()
        speedTable[elem[0]] = (int(elem[3]), int(elem[6]), int(elem[13]))
    return speedTable

def speedTableToDistance(speedTable: tuple, seconds: int):
    full, last = divmod(seconds, speedTable[1]+speedTable[2])
    return (full*speedTable[1] + min(last, speedTable[1]))*speedTable[0]

def part1(scheme: list, seconds: int):
    speedTable = generateSpeedTable(scheme)
    return {k:speedTableToDistance(v, seconds) for k, v in speedTable.items()}

def part2(scheme: list, seconds: int):
    speedTable = generateSpeedTable(scheme)
    winners = list()
    for second in range(1, seconds+1):
        iteration = part1(scheme, second)
        maximum = max(iteration.values())
        winners = winners + [k for k in iteration if iteration[k] == maximum]
    return {k:winners.count(k) for k in speedTable}

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.', 'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
        expectedSpeedTable = {'Comet': (14, 10, 127), 'Dancer': (16, 11, 162)}
        self.assertDictEqual(expectedSpeedTable, generateSpeedTable(testInput))
        expectedResultP1 = {'Comet': 1120, 'Dancer': 1056}
        self.assertDictEqual(expectedResultP1, part1(testInput, 1000))
        expectedResultP2 = {'Comet': 312, 'Dancer': 689}
        self.assertDictEqual(expectedResultP2, part2(testInput, 1000))

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 2503)
    print(f"Part 1: {max(p1.values())}")
    p2 = part2(scheme, 2503)
    print(f"Part 2: {max(p2.values())}")
    print(time()-a)

