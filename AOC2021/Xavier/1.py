import re
import time
from collections import defaultdict
from math import sqrt


def readFile(filePath):
    fileIn = open(filePath)
    for line in fileIn:
        instructions = [l.rstrip().lstrip() for l in line.split(",")]
        break
    return instructions

def update_direction(posInd, instruction):
    if instruction == 'L':
        posInd = (posInd - 1) % 4
    elif instruction == 'R':
        posInd = (posInd + 1) % 4
    
    return posInd

if __name__ == '__main__' :
    start = time.time()

    instructions = readFile("inputs/01.txt")
    
    directions = [ [0,1], [1,0], [0,-1], [-1,0] ]
    posInd = 0
    pos = [0,0]
    
    grid = []
    for k in range(500):
        grid.append([0] * 500)
    
    found = False
    for instr in instructions:
        posInd = update_direction(posInd, instr[0])
        
        print(pos, instr, directions[posInd], end="  ->  ")
        for k in range(int("".join(instr[1:] ))):
            for i in range(2):
                pos[i] += directions[posInd][i]

            grid[pos[0]][pos[1]] += 1
            if grid[pos[0]][pos[1]] >=2 :
                print("Found twice: ", pos, sum([abs(k) for k in pos]))
                found = True
        print(pos)

        if found:
            break

    print("Result: ", sum([abs(k) for k in pos]))


    
    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
