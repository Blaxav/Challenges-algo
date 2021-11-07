import re
import time
from collections import defaultdict
from math import sqrt

if __name__ == '__main__' :
    start = time.time()

    digits = [  ['0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '1', '0', '0', '0'],
                ['0', '0', '2', '3', '4', '0', '0'],
                ['0', '5', '6', '7', '8', '9', '0'],
                ['0', '0', 'A', 'B', 'C', '0', '0'],
                ['0', '0', '0', 'D', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0'] ]

    pos = [3,1]
    code = []

    fileIn = open("inputs/02.txt")
    for line in fileIn:
        for instr in line.strip():
            if instr == "D":
                if digits[pos[0] + 1][pos[1]] != '0':
                    pos[0] = pos[0] + 1
            elif instr == "U":
                if digits[pos[0] - 1][pos[1]] != '0':
                    pos[0] = max(pos[0] - 1, 0)
            elif instr == "L":
                if digits[pos[0]][pos[1] - 1] != '0':
                    pos[1] = pos[1] - 1
            elif instr == "R":
                if digits[pos[0]][pos[1] + 1] != '0':
                    pos[1] = pos[1] + 1
        code.append(digits[pos[0]][pos[1]])

    print("Code: ", code )

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
