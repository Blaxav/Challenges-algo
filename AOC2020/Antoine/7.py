from time import time
from collections import defaultdict, deque
import unittest
import re
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().replace(".","") for i in f.readlines()]

def parseScheme(scheme:list):
    containBagsDict = defaultdict(dict)
    for instruction in scheme:
        if "no other" not in instruction:
            container, *contained = re.split(' contain |, ', instruction)
            for bag in contained:
                bag = bag.split()
                containBagsDict[container[:-5]][bag[1] + " " + bag[2]] = int(bag[0])
    
    return containBagsDict

def exploreBags(bag: str, containBagsDict: dict, amountOfBag: int):
    if bag not in containBagsDict:
        return 1
    else:
        return amountOfBag + sum(exploreBags(containedBag, containBagsDict, 1) * amount for containedBag, amount in containBagsDict[bag].items())
            
def part1(scheme: list):
    containBagsDict = parseScheme(scheme)
    bags, resBags = deque(["shiny gold"]), list()
    while bags:
        currentBag = bags.pop()
        for bag, containedBags in containBagsDict.items():
            if currentBag in containedBags:
                if bag not in bags:
                    bags.append(bag)
                if bag not in resBags:
                    resBags.append(bag)

    return len(resBags)

def part2(scheme: list):
    containBagsDict = parseScheme(scheme)

    return exploreBags("shiny gold", containBagsDict, 0)

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

