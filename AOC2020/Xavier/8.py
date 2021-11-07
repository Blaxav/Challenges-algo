import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers


def read_file(instructions):
    fileIn = open(sys.argv[1])
    for line in fileIn:
        line = line.rstrip().split()
        instructions.append( (line[0], int(line[1]) ) )
    

class Program:
    def __init__(self):
        self.acc = 0
        self.offset = 0
    
    def reset(self):    
        self.acc = 0
        self.offset = 0

    def apply(self, instr):
        var, val = instr
        if var == "acc":
            self.acc += val
            self.offset += 1
        elif var =="jmp":
            self.offset += val
        elif var == "nop":
            self.offset += 1
    
    def run(self, instructions):
        instr_done = [0] * len(instructions)

        while True:
            instr = instructions[self.offset]
            instr_done[self.offset] += 1
            self.apply(instr)

            if self.offset == len(instructions):
                return True

            if instr_done[self.offset] > 0 :
                return False    

if __name__ == '__main__' :
    start = time.time()

    instructions = []
    read_file(instructions)
    
    prog = Program()
    final_acc = prog.run(instructions)
    print("Result part 1: ", prog.acc)

    command = ["jmp", "nop"]
    for k in range(len(instructions)):
        
        prog.reset()
        var, val = instructions[k]
        if var in command:
            newVar =command[ (command.index(var) + 1) % 2 ]
            instructions[k] = (newVar, val)

            

            if prog.run(instructions):
                print("Change index ", k, prog.acc)
                print("Success. Final accumulator: ", prog.acc)
                break
            
            instructions[k] = (var, val)
        
            


    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
