import time
from collections import defaultdict
from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)

if __name__ == '__main__' :
    start = time.time()

    current = 1
    length = 0

    total = 1.0
    primesCnt = 0.0

    maxSize = 7

    while length == 0 or (primesCnt / total) > 0.1000:
        length += 2

        for i in range(4):
            current += length
            total += 1
            #print("%-10i%-10i" % (current, total))
            if is_prime(current):
                primesCnt += 1.0
        if length % 1000 == 0:
            print("%-12i%10i/%-10i%-12.3f" % (length + 1, primesCnt, total,  primesCnt / total))
        
        
    
    print("Result: ", length + 1)
    print( primesCnt /total )
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
