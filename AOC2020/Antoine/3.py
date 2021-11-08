from time import time
from math import ceil
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def extendScheme(scheme: list, slopeX: int, slopeY: int):
    height = len(scheme)
    minimumExpectedWidth = height * (slopeY / slopeX)
    return [a * ceil(minimumExpectedWidth / len(scheme[0])) for a in scheme]

            
def part1(scheme: list, slopeX: int, slopeY: int):
    extendedScheme = extendScheme(scheme, slopeX, slopeY)
    x, y, treeCount = 0, 0, 0
    while x < len(extendedScheme):
        treeCount += 1 if extendedScheme[x][y] == "#" else 0
        x += slopeX
        y += slopeY
    return treeCount

def part2(scheme: list):
    treeProd, slopes = 1, [(1,1),(1,3),(1,5),(1,7),(2,1)]
    for slope in slopes:
        treeProd *= part1(scheme, *slope)
    return treeProd

class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]
        self.assertEqual(part1(testInput, 1, 3), 7)
        self.assertEqual(part2(testInput), 336)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 1, 3)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

