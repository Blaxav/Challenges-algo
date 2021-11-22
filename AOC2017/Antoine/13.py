from time import time
import unittest
from itertools import cycle
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return {int(i.strip().split(': ')[0]):int(i.strip().split(': ')[1]) for i in f.readlines()}

def is_scanner_at_zero_position(time: int, size: int, delay: int):
    return (time + delay) % ((size - 1) * 2) == 0
            
def part1(scheme: dict):
    return sum(k*v for k, v in scheme.items() if is_scanner_at_zero_position(k, v, 0))

def is_packet_caught(scheme: dict, delay: int):
    for k, v in scheme.items():
        if is_scanner_at_zero_position(k, v, delay):
            return False
    
    return True
    # return sum(1 for k, v in scheme.items() if is_scanner_at_zero_position(k, v, delay))

def part2(scheme: list):
    delay = 0
    while not is_packet_caught(scheme, delay):
        delay += 1

    return delay

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

