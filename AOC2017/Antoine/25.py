from collections import defaultdict
from time import time
import re
import unittest
import json
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines() if i.strip()]

def parse_scheme(scheme: list):
    it = 0
    states = dict()
    current_state_actions = defaultdict(dict)
    mapping_instruction = {"0": 0, "1": 1, "left": -1, "right": 1}
    while it in range(len(scheme)):
        instruction = scheme[it]
        if instruction.startswith("Begin"):
            first_state = instruction[-2]
            it += 1
        elif instruction.startswith("Perform"):
            steps = int(re.findall('[0-9]+', instruction)[0])
            it += 1
        elif instruction.startswith("In"):
            current_state = instruction[-2]
            it += 1
        elif instruction.startswith("If"):
            current_value = int(instruction[-2])
            it += 1
        else:
            split_instruction = instruction.replace('.', '').split(' ')
            current_state_actions[current_value][split_instruction[1]] = mapping_instruction[split_instruction[-1]] if split_instruction[-1] in mapping_instruction else split_instruction[-1]
            it += 1
            if current_value == 1 and split_instruction[1] == "Continue":
                states[current_state] = current_state_actions
                current_state_actions = defaultdict(dict)
    
    return first_state, steps, states

class Tape:
    def __init__(self, first_state) -> None:
        self.tape = defaultdict(int)
        self.current_state = first_state
        self.cursor = 0
    
    def evol(self, states):
        initial_value = self.tape[self.cursor]
        self.tape[self.cursor] = states[self.current_state][initial_value]["Write"]
        self.cursor += states[self.current_state][initial_value]["Move"]
        self.current_state = states[self.current_state][initial_value]["Continue"]

            
def part1(first_state: str, steps: int, states: dict):
    tape = Tape(first_state)
    for it in range(steps):
        tape.evol(states)
    
    return sum(tape.tape.values())

def part2(scheme: list):
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    first_state, steps, states = parse_scheme(scheme)
    p1 = part1(first_state, steps, states)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

