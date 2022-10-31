from time import time
import unittest
from sympy import cos, sin, pi
from collections import defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def generate_map(scheme: list):
    scheme_length = len(scheme)
    map = defaultdict(lambda: 'C')
    for y, line in enumerate(scheme):
        for x, char in enumerate(line):
            if char == '#':
                map[(x, scheme_length - y - 1)] = 'I'
    
    return map

class Virus_carrier:
    def __init__(self, map, scheme):
        self.orientation = [0, 1]
        self.x = (len(scheme) - 1) // 2
        self.y = (len(scheme) - 1) // 2
        self.bursts = 0
        self.map = map

    def turn(self, part: int):
        current_node = self.map[(self.x, self.y)]
        if part == 1:
            if current_node == 'I':
                angle = -pi/2
            else:
                angle = pi/2
        elif part == 2:
            if current_node == 'C':
                angle = pi/2
            elif current_node == 'W':
                angle = 0
            elif current_node == 'I':
                angle = -pi/2
            else:
                angle = pi
        
        self.orientation = [self.orientation[0] * cos(angle) - self.orientation[1] * sin(angle), self.orientation[0] * sin(angle) + self.orientation[1] * cos(angle)]
    
    def infect(self, part: int):
        current_node = self.map[(self.x, self.y)]
        if part == 1:
            if current_node == 'I':
                del self.map[(self.x, self.y)]
            else:
                self.map[(self.x, self.y)] = 'I'
                self.bursts += 1
        elif part == 2:
            if current_node == 'C':
                self.map[(self.x, self.y)] = 'W'
            elif current_node == 'W':
                self.map[(self.x, self.y)] = 'I'
                self.bursts += 1
            elif current_node == 'I':
                self.map[(self.x, self.y)] = 'F'
            else:
                del self.map[(self.x, self.y)]

    
    def move(self):
        self.x += self.orientation[0]
        self.y += self.orientation[1]

    def step(self, part: int):
        self.turn(part)
        self.infect(part)
        self.move()


def part1(scheme: list):
    map = generate_map(scheme)
    virus_carrier = Virus_carrier(map, scheme)
    for it in range(10_000):
        virus_carrier.step(1)

    return virus_carrier.bursts

def part2(scheme: list):
    map = generate_map(scheme)
    virus_carrier = Virus_carrier(map, scheme)
    for it in range(10_000_000):
        virus_carrier.step(2)

    return virus_carrier.bursts

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

