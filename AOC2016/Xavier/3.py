import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    fileIn = open(sys.argv[1])

    valid = True
    totalValid = 0

    innerCounter = 0
    triangles = [[],[],[]]
    validP2 = 0

    for line in fileIn:
        sides = [int(i) for i in line.split()]
        valid = True
        
        # Part 1
        for k in range(3):
            if sides[k] + sides[(k+1) % 3] <= sides[(k+2) % 3] :
                valid = False
                break
        if valid:
            totalValid += 1
        
        # Part 2
        for t in range(3):
            triangles[t].append(sides[t])
            innerCounter += 1

        if innerCounter == 9:
            for t in range(3):
                valid = True
                for k in range(3):
                    if triangles[t][k] + triangles[t][(k+1) % 3] <= triangles[t][(k+2) % 3] :
                        valid = False
                        break

                if valid:
                    validP2 += 1
                
                triangles[t].clear()
                innerCounter = 0

    print("Result P1: ", totalValid)
    print("Result P2: ", validP2)

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
