from time import time
import unittest
from collections import defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(it) for it in i.replace(' -> ', ',').split(',')] for i in f.readlines()]

            
def part1(scheme: list):
    positions = defaultdict(int)
    for wind in scheme:
        if wind[0] == wind[2]:
            min_y, max_y = min(wind[1], wind[3]), max(wind[1], wind[3]) + 1
            for y in range(min_y, max_y):
                positions[(wind[0], y)] += 1
        elif wind[1] == wind[3]:
            min_x, max_x = min(wind[0], wind[2]), max(wind[0], wind[2]) + 1
            for x in range(min_x, max_x):
                positions[(x, wind[1])] += 1

    return sum(1 for v in positions.values() if v > 1)

def part2(scheme: list):
    positions = defaultdict(int)
    for wind in scheme:
        if wind[0] == wind[2]:
            min_y, max_y = min(wind[1], wind[3]), max(wind[1], wind[3]) + 1
            for y in range(min_y, max_y):
                positions[(wind[0], y)] += 1
        elif wind[1] == wind[3]:
            min_x, max_x = min(wind[0], wind[2]), max(wind[0], wind[2]) + 1
            for x in range(min_x, max_x):
                positions[(x, wind[1])] += 1
        elif abs(wind[0] - wind[2]) == abs(wind[1] - wind[3]):
            diff_for_range = abs(wind[0] - wind[2]) + 1
            for it in range(diff_for_range):
                positions[(wind[0] + (1 if wind[2] > wind[0] else -1) * it, wind[1] + (1 if wind[3] > wind[1] else -1) * it)] += 1

    return sum(1 for v in positions.values() if v > 1)

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

