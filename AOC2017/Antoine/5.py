from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i.strip()) for i in f.readlines()]

            
def part1(scheme: list):
    current_index, steps = 0, 0
    while current_index in range(len(scheme)):
        scheme[current_index] += 1
        current_index += scheme[current_index] - 1
        steps += 1
    return steps

def part2(scheme: list):
    current_index, steps = 0, 0
    while current_index in range(len(scheme)):
        jump = 1 if scheme[current_index] < 3 else -1
        scheme[current_index] += jump
        current_index += scheme[current_index] - jump
        steps += 1
    return steps

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

