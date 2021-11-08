from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def arithmeticProgression(n: int):
    return n*(n-1)*0.5 + 1

def getOrder(row: int, col: int):
    return arithmeticProgression(row+col-1) + col - 1
            
def part1(scheme: list):
    scheme = scheme.split()
    row, col = int(scheme[15][:-1]), int(scheme[17][:-1])
    order = int(getOrder(row, col))
    start = 20151125
    for it in range(1, order):
        start = (start*252533) % 33554393
    return start

def part2(scheme: list):
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        arithmeticTest = [1, 2, 4, 7, 11, 16]
        for num, elem in enumerate(arithmeticTest, 1):
            self.assertEqual(arithmeticProgression(num), elem)
        self.assertEqual(getOrder(4, 3), 18)
        self.assertEqual(getOrder(4, 2), 12)
        self.assertEqual(getOrder(1, 5), 15)



if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

