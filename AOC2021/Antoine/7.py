from time import time
import unittest
from math import inf
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(it) for it in f.readline().strip().split(',')]

            
def part1(scheme: list):
    best_fuel_consumption = inf
    for it in range(min(scheme), max(scheme) + 1):
        current_fuel_consumption = sum([abs(it - elem) for elem in scheme])
        if best_fuel_consumption > current_fuel_consumption:
            best_fuel_consumption = current_fuel_consumption

    return best_fuel_consumption

def part2(scheme: list):
    best_fuel_consumption, sums = inf, {k:sum(range(k + 1)) for k in range(min(scheme), max(scheme) + 1)}
    for it in range(min(scheme), max(scheme) + 1):
        current_fuel_consumption = sum((sums[abs(it - elem)] for elem in scheme))
        if best_fuel_consumption > current_fuel_consumption:
            best_fuel_consumption = current_fuel_consumption

    return best_fuel_consumption

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

