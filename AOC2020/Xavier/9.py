import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    fileIn = open(sys.argv[1])
    k = 0
    sizeT = 25
    found =  False
    allNums = []
    wrongVal = 0

    for line in fileIn:
        val = int(line.rstrip())
        found = False
        if k >= sizeT :
            for i in range(k - sizeT, len(allNums)):
                for j in range(i+1, len(allNums)):
                    if allNums[i] + allNums[j] == val:
                        found = True
                        break
                if found:
                    break

            if not found:
                print("Part1: ", val, " iteration: ", k)
                wrongVal = val
                break

        allNums.append(val)
        k += 1

    imin = 0
    imax = 1
    found = False
    while not found:
        if sum(allNums[imin:imax]) < wrongVal:
            imax += 1
        elif sum(allNums[imin:imax]) > wrongVal:
            imin += 1
        else :
            found = True

    print("Part2: ", imin, imax, sum(allNums[imin:imax]) )
    print("Result: ", min(allNums[imin:imax]) + max(allNums[imin:imax]) )

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
