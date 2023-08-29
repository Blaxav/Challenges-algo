from time import time
import unittest
from itertools import cycle
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]
            
def part1(scheme: list):
    return sum(scheme)

def part2(scheme: list):
    count = 0
    frequencies = set()
    current_frequency = 0
    for change in cycle(scheme):
        if current_frequency in frequencies:
            return current_frequency
        else:
            count += 1
            frequencies.add(current_frequency)
            current_frequency += change
    
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

