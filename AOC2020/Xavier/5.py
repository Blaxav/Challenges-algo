import re
import time
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()


    fileIn = open("input_5.txt")

    maxId = 0
    minId = 1e6
    l = [0] * (127*8)
    for line in fileIn :
        passId = line.rstrip()

        rows = passId[:7]
        seats = passId[7:]
        
        minRow = 0
        maxRow = 127
        for car in rows:
            if car == "F":
                maxRow = int( (maxRow + minRow + 1) / 2 ) - 1
            else :
                minRow = int( (maxRow + minRow + 1) / 2 )

        minSeat = 0
        maxSeat = 7
        for car in seats:
            if car == "L":
                maxSeat = int( (maxSeat + minSeat + 1) / 2 ) - 1
            else :
                minSeat = int( (maxSeat + minSeat + 1) / 2 )
        
        cId = 8 * minRow + minSeat
        if cId > maxId :
            maxId = cId

        if cId < minId:
            minId = cId
        l[cId] = 1
    
    l = l[minId:]
    seat = l.index(0) + minId
    print("Your sit is: ", seat)

    print("MaxId: ", maxId)
    print("MinId: ", minId)
    
    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
