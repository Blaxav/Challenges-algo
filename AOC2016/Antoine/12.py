from time import time
from collections import defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def is_num(s: str):
    try:
        int(s)
    except:
        return False
    return True

def getval(regs: dict, x: str):
    if is_num(x):
        return int(x)
    else:
        return regs[x]
            
def part1(scheme: list, first_input: int):
    it, register = 0, {'a': 0, 'b': 0, 'c': first_input, 'd': 0}
    while it in range(len(scheme)):
        instruction = scheme[it].split()
        if instruction[0] == "cpy":
            val_to_copy = getval(register, instruction[1])
            register[instruction[2]] = val_to_copy
            it += 1
        elif instruction[0] == "inc":
            register[instruction[1]] += 1
            it += 1
        elif instruction[0] == "dec":
            register[instruction[1]] -= 1
            it += 1
        elif instruction[0] == "jnz":
            val_to_test, val_to_jump = getval(register, instruction[1]), getval(register, instruction[2])
            if val_to_test:
                it += val_to_jump
            else:
                it += 1

    return register['a']

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 0)
    print(f"Part 1: {p1}")
    p2 = part1(scheme, 1)
    print(f"Part 2: {p2}")
    print(time()-a)

