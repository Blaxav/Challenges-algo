from time import time
from hashlib import md5
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline()

def calculateHash(stringInput: str, iterations: int):
    res = stringInput
    for iteration in range(iterations):
        res = md5(res.encode('utf-8')).hexdigest()
    return res

def threeConsecutiveChars(stringInput: str):
    for ind in range(len(stringInput)-2):
        if stringInput[ind] == stringInput[ind+1] == stringInput[ind+2]:
            return stringInput[ind]
    return None

def hasThisFiveConsecutiveChars(stringInput: str, expectedChar: str):
    if expectedChar * 5 in stringInput:
        return True
    else:
        return False

def generateHashDict(stringInput: str, iterations: int, limit: int):
    return {k:calculateHash(stringInput+str(k), iterations) for k in range(limit)}


def part1(scheme: str):
    comp, indexes, hashes = 0, list(), generateHashDict(scheme, 1, 30000)
    while len(indexes) != 64:
        triplet = threeConsecutiveChars(hashes[comp])
        if triplet:
            for secondComp in range(comp+1, comp+1001):
                if hasThisFiveConsecutiveChars(hashes[secondComp], triplet):
                    indexes.append(comp)
                    break
        comp += 1
    return indexes[-1]

def part2(scheme: list):
    comp, indexes, hashes = 0, list(), generateHashDict(scheme, 2017, 30000)
    while len(indexes) != 64:
        triplet = threeConsecutiveChars(hashes[comp])
        if triplet:
            for secondComp in range(comp+1, comp+1001):
                if hasThisFiveConsecutiveChars(hashes[secondComp], triplet):
                    indexes.append(comp)
                    break
        comp += 1
    return indexes[-1]

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1("abc"), 22728)
        self.assertEqual(part2("abc"), 22551)

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

