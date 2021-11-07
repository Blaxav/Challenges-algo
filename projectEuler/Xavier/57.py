import time
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)


def frac_u():
    u = Fraction(1, 2)
    while True:
        num = u.numerator
        denom = u.denominator
        u = Fraction(denom, 2*denom + num)
        yield u

def frac_sqrt():
    g = frac_u()
    
    while True:
        u = next(g)
        yield Fraction(u.denominator + u.numerator, u.denominator)


if __name__ == '__main__' :
    start = time.time()

    g = frac_sqrt()
    it = 2
    cnt = 0

    while it < 1000:
        frac = next(g)

        if it == 8:
            print(frac)

        if len(str(frac.numerator)) > len(str(frac.denominator)):
            cnt += 1

        it += 1

    print("Result: ", cnt)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
