from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def generateSueTable(scheme:list):
    sueTable = dict()
    for elem in scheme:
        elem = elem.replace(':', '').replace(',', '')
        elem = elem.split()
        sueTable[int(elem[1])] = {elem[2]: int(elem[3]), elem[4]: int(elem[5]), elem[6]: int(elem[7])}
    return sueTable

def dictContainDict(dictOne: dict, dictTwo: dict):
    for key in dictTwo:
        if dictOne[key] != dictTwo[key]:
            return False
    return True

def part1(scheme: list):
    sueTable = generateSueTable(scheme)
    realSue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
    for res, sue in enumerate(sueTable.values(), 1):
        if dictContainDict(realSue, sue):
            return res
    return 0

def dictSatisfiesConditions(dictOne: dict, dictTwo: dict):
    for key in dictTwo:
        if key in ['cats', 'trees']:
            if dictOne[key] >= dictTwo[key]:
                return False
        elif key in ['pomeranians', 'goldfish']:
            if dictOne[key] <= dictTwo[key]:
                return False
        else:
            if dictOne[key] != dictTwo[key]:
                return False
    return True

def part2(scheme: list):
    sueTable = generateSueTable(scheme)
    realSue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
    for res, sue in enumerate(sueTable.values(), 1):
        if dictSatisfiesConditions(realSue, sue):
            return res
    return 0

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

