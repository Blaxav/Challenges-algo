import time
from collections import defaultdict
#from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)

if __name__ == '__main__' :
    start = time.time()

    periods = []
    offsets = []
    cnt = 0
    fileIn = open("aoc2016_15.txt")
    for line in fileIn:
        periods.append( int(line.split()[3]) ) 
        offsets.append( ( int(line.split()[-1][:-1]) + cnt) % periods[cnt]  )
        cnt += 1
    
    it = 0
    while max(offsets) > 0:
        for k in range(cnt):
            offsets[k] = (1 + offsets[k] ) % periods[k]
        it += 1
        if it % 100000 == 0:
            print(it, offsets)
    print(it, offsets)


    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
