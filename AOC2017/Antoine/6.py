from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(it) for it in f.readline().strip().split('\t')]

            
def part1(scheme: list):
    configurations, cycles = [], 0
    while scheme not in configurations:
        configurations.append(scheme[:])
        max_blocks = max(scheme)
        max_index = scheme.index(max_blocks)
        scheme[max_index] = 0
        for it in range(1, max_blocks + 1):
            scheme[max_index + it if max_index + it < len(scheme) else max_index + it - len(scheme)] += 1
        cycles += 1
    return cycles, configurations, scheme

def part2(configurations: list, last_scheme: list):
    return len(configurations) - configurations.index(last_scheme)

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1[0]}")
    p2 = part2(p1[1], p1[2])
    print(f"Part 2: {p2}")
    print(time()-a)

