import time
from collections import defaultdict
from functools import lru_cache
from math import sqrt

from utils import add_one, is_prime, prime_numbers


@lru_cache(maxsize = None)
def binom(k,n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    if k == 0 or k == n:
        return 1
    
    return binom(k, n-1) + binom(k-1, n-1)

if __name__ == '__main__' :
    start = time.time()

    cnt = 0
    for n in range(101):
        for k in range(n+1):
            if binom(k,n) >= 1e6:
                cnt += 1

    print("Result: ", cnt)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
