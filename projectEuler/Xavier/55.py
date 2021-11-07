import time
from collections import defaultdict
from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)

if __name__ == '__main__' :
    start = time.time()

    total = 0
    for n in range(1, 10001):
        it = 0
        cur = n
        while it < 50:
            cur += int( str(cur)[::-1] )
            if str(cur) == str(cur)[::-1]:
                total += 1
                break
            it += 1
        
    print("Result: ", 10000 - total)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
