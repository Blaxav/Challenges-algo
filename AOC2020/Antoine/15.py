from time import time
from collections import defaultdict, deque
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        line = f.readline().strip()
        return [int(elem) for elem in line.split(',')]

            
# def part1(scheme: list, end: int):
#     spokenDict = dict()
#     for it in range(1, end+1):
#         if it <= len(scheme):
#             spokenDict[it] = scheme[it-1]
#         else:
#             lastSpoken = spokenDict[it-1]
#             if list(spokenDict.values()).count(lastSpoken) == 1:
#                 spokenDict[it] = 0
#             else:
#                 max1, max2 = sorted([elem for elem, value in spokenDict.items() if value == lastSpoken], reverse=True)[:2]
#                 spokenDict[it] = max1- max2

#     return spokenDict[end]

def part1(scheme: list, end: int):
    spokenDict = defaultdict(deque)
    for it in range(1, end+1):
        if it <= len(scheme):
            spokenDict[scheme[it-1]].appendleft(it)
            lastSpoken = scheme[it-1]
        else:
            if len(spokenDict[lastSpoken]) == 1:
                lastSpoken = 0
                if len(spokenDict[lastSpoken]) == 2:
                    trash = spokenDict[lastSpoken].pop()
                spokenDict[lastSpoken].appendleft(it)
            else:
                lastSpoken = spokenDict[lastSpoken][0] - spokenDict[lastSpoken][1]
                if len(spokenDict[lastSpoken]) == 2:
                    trash = spokenDict[lastSpoken].pop()
                spokenDict[lastSpoken].appendleft(it)

    return lastSpoken

def part2(scheme: list):
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 2020)
    print(f"Part 1: {p1}")
    p2 = part1(scheme, 30000000)
    print(f"Part 2: {p2}")
    print(time()-a)

