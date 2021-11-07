import time
from collections import defaultdict
from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)


def mul(l, a):
    for k in range(len(l)):
        l[k] *= a

    propagate_left_to_right(l)


if __name__ == '__main__' :
    start = time.time()

    sumVal = 0
    maxSum = 0

    for n in range(1, 100):
        l = [1]
        for b in range(1, 100):
            mul(l, n)
            if sum(l) > maxSum:
                maxSum = sum(l)
                print(n ,b , l, n**b, maxSum)


    print("Max: ", sum([int(i) for i in str(94**98)]) )
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
