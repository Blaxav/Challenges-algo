from time import time
import unittest
from collections import defaultdict
import re
from math import sqrt
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.split() for i in f.readlines()]
        
class Register:
    def __init__(self):
        self.register = defaultdict(int)
        self.cursor = 0
        self.count_mul = 0
        self.loops = defaultdict(int)
    
    def get_value(self, arg):
        if re.match('[\-0-9]', arg):
            return int(arg)
        else: 
            return self.register[arg]

    def operation(self, operation, arg1, arg2):
        if operation == 'jnz':
            if self.get_value(arg1):
                if self.get_value(arg2) < 0:
                    self.loops[self.cursor] += 1
                self.cursor += self.get_value(arg2)
            else:
                self.cursor += 1
        else:
            if operation == 'set':
                self.register[arg1] = self.get_value(arg2)
            elif operation == 'sub':
                self.register[arg1] -= self.get_value(arg2)
            elif operation == 'mul':
                self.register[arg1] *= self.get_value(arg2)
                self.count_mul += 1
            self.cursor += 1
        
    def make_instruction(self, instruction):
        self.operation(instruction[0], instruction[1], instruction[2])

    
def part1(scheme: list):
    register = Register()
    while register.cursor in range(len(scheme)):
        register.make_instruction(scheme[register.cursor])

    return register.count_mul

def part2():
    count_h = 0
    for b in range(105_700, 122_700 + 17, 17):
        for d in range(2, int(sqrt(b))):
            if b % d == 0:
                count_h += 1
                break

    return count_h

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2()
    print(f"Part 2: {p2}")
    print(time()-a)

