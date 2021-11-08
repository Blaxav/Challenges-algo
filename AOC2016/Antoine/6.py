from time import time
import unittest
from collections import defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]
 
def part1(scheme: list):
    message = ''
    for it in range(8):
        counter = [elem[it] for elem in scheme]
        message += max(counter,key=counter.count)
    return message

def part2(scheme: list):
    message = ''
    for it in range(8):
        counter = [elem[it] for elem in scheme]
        message += min(counter,key=counter.count)
    return message

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

