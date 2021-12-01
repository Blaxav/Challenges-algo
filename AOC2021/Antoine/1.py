from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]

            
def part1(scheme: list):
    current_elem, increase_amount = scheme[0], 0
    for it in range(1, len(scheme)):
        if scheme[it] > current_elem:
            increase_amount += 1
        current_elem = scheme[it]

    return increase_amount

def part2(scheme: list):
    sliding_measures = [sum(scheme[it:it+3]) for it in range(len(scheme)-2)]
    
    return part1(sliding_measures)

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

