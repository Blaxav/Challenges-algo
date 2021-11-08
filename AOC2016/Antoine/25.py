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


def iteration(scheme: list, first_input: int):
    it, register, out_values = 0, {'a': first_input, 'b': 0, 'c': 0, 'd': 0}, []
    while it in range(len(scheme)):
        if len(out_values) == 10:
            return out_values
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
        elif instruction[0] == "out":
            out_values.append(getval(register, instruction[1]))
            it += 1

def part1(scheme: list):
    first_input = 0
    while True:
        out_values = iteration(scheme[:], first_input)
        if out_values == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:
            return first_input
        else:
            first_input += 1

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1= part1(scheme[:])
    print(f"Part 1: {p1}")
    # p2 = part2(scheme[:], 12)
    # print(f"Part 2: {p2['a']}")
    print(time()-a)

