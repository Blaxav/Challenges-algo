from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().replace('   ', ' ').replace('  ', ' ').split(' ') for i in f.readlines()]

def isTriangle(triangle: list):
    sides = [int(a) for a in triangle]
    sides.sort()
    return int(sides[0] + sides[1] > sides[2])
            
def part1(scheme: list):
    count = 0
    for elem in scheme:
        count += isTriangle(elem)
    return count

def part2(scheme: list):
    count = 0
    padding = 0
    while padding < len(scheme):
        verticalTriangles = scheme[padding:padding+3]
        for it in range(3):
            count += isTriangle([elem[it] for elem in verticalTriangles])
        padding += 3
    return count

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

