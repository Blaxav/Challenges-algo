import re
import sys
import time
from collections import defaultdict
from math import sqrt
from functools import lru_cache

from utils import add_one, is_prime, prime_numbers


########################################################################################
# Defining the list as global to use it in the cache
fileIn = open(sys.argv[1])
values = [0]
for line in fileIn:
    values.append(int(line))

values.sort()
#add device
values.append(values[-1] + 3)

########################################################################################
# Recursive function
@lru_cache(maxsize = None)
def following(n):
    if n == values[-1]:
        return 1
    else:
        total = 0
        index = values.index(n)
        maxIndex = min(index + 4, len(values) )
        for k in range(index + 1, maxIndex):
            if values[k] <= (n + 3):
                total += following(values[k])
            else :
                break
        #print(n, total)
        return total

########################################################################################
# Main
if __name__ == '__main__' :
    start = time.time()
    
    diffs = [ values[i] - values[i-1] for i in range(1, len(values))]
    distrib_diffs = []
    for i in range(4):
        distrib_diffs.append( len( [x for x in diffs if x == i] ) )
    
    print("Distribution des differences: ", distrib_diffs)
    print("Result p1: ", distrib_diffs[1] * distrib_diffs[3])

    print("Result p2: ", following(0) )


    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
