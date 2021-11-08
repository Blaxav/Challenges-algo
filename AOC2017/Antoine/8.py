from time import time
import unittest
from collections import defaultdict
from math import inf
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().split() for i in f.readlines()]

def treat_instruction(instruction: list, register: defaultdict):
    coefficient_dict = {'dec': -1, 'inc': 1}
    if instruction[5] == '<' and register[instruction[4]] < int(instruction[6]):
        register[instruction[0]] += coefficient_dict[instruction[1]] * int(instruction[2])
    elif instruction[5] == '>' and register[instruction[4]] > int(instruction[6]):
        register[instruction[0]] += coefficient_dict[instruction[1]] * int(instruction[2])
    elif instruction[5] == '<=' and register[instruction[4]] <= int(instruction[6]):
        register[instruction[0]] += coefficient_dict[instruction[1]] * int(instruction[2])
    elif instruction[5] == '>=' and register[instruction[4]] >= int(instruction[6]):
        register[instruction[0]] += coefficient_dict[instruction[1]] * int(instruction[2])
    elif instruction[5] == '==' and register[instruction[4]] == int(instruction[6]):
        register[instruction[0]] += coefficient_dict[instruction[1]] * int(instruction[2])
    elif instruction[5] == '!=' and register[instruction[4]] != int(instruction[6]):
        register[instruction[0]] += coefficient_dict[instruction[1]] * int(instruction[2])

    return register
            
def part1(scheme: list):
    register = defaultdict(int)
    for instruction in scheme:
        register = treat_instruction(instruction, register)

    return max(register.values())

def part2(scheme: list):
    register, max_process_value = defaultdict(int), -inf
    for instruction in scheme:
        register = treat_instruction(instruction, register)
        if max(register.values()) > max_process_value:
            max_process_value = max(register.values())
    return max_process_value

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

