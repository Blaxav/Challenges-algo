from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(it) for i in f.readlines() for it in i.split(',')]

            
def part1(scheme: list):
    lanternfishes = {k: scheme.count(k) for k in range(9)}
    for it in range(80):
        stored_zero = lanternfishes[0] 
        for number in range(8):
            lanternfishes[number] = lanternfishes[number + 1]
        lanternfishes[8] = stored_zero
        lanternfishes[6] += stored_zero
        
    return sum(lanternfishes.values())

def part2(scheme: list):
    lanternfishes = {k: scheme.count(k) for k in range(9)}
    for it in range(256):
        stored_zero = lanternfishes[0] 
        for number in range(8):
            lanternfishes[number] = lanternfishes[number + 1]
        lanternfishes[8] = stored_zero
        lanternfishes[6] += stored_zero

    return sum(lanternfishes.values())

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme[:])
    print(f"Part 1: {p1}")
    p2 = part2(scheme[:])
    print(f"Part 2: {p2}")
    print(time()-a)

