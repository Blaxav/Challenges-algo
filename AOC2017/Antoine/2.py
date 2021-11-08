from time import time
from itertools import product
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(number) for number in i.strip().split('\t')] for i in f.readlines()]

            
def part1(scheme: list):
    checksum = 0
    for elem in scheme:
        checksum += max(elem) - min(elem)
    return checksum

def part2(scheme: list):
    checksum = 0
    for elem in scheme:
        sorted_elem = sorted(elem)
        reverse_sorted_elem = sorted_elem[::-1]
        for high_number, low_number in product(reverse_sorted_elem, sorted_elem):
            if high_number % low_number == 0 and high_number != low_number:
                checksum += high_number // low_number
                break
    return checksum

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

