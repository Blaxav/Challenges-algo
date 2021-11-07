import time
from collections import defaultdict
from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)


def pentag():
    i = 0
    while True:
        i += 1
        yield int(i*(3*i-1)/2)

def triang():
    i = 0
    while True:
        i += 1
        yield int(i*(i+1)/2)

def square():
    i = 0
    while True:
        i += 1
        yield int(i*i)

def hexa():
    i = 0
    while True:
        i += 1
        yield int(i*(2*i-1))

def hepta():
    i = 0
    while True:
        i += 1
        yield int(i*(5*i-3)/2)

def octo():
    i = 0
    while True:
        i += 1
        yield int(i*(3*i-2))

def init_beginlist(dic, gen):
    g = gen()
    p = next(g)
    while p < 1000:
        p = next(g)

    while p < 10000:
        dic[str(p)[:2]].append(p)
        p = next(g)


if __name__ == '__main__' :
    start = time.time()

    begins = {}
    gens = {3: triang, 4: square, 5: pentag, 6: hexa, 7: hepta, 8: octo}
    for k in [3,4,5,6,7,8]:
        begins[k] = defaultdict(lambda: [])
    
    for k in [3,4,5,6,7,8]:
        init_beginlist(begins[k], gens[k])
    

    for beg in begins[3]:
        for first in begins[3][beg]:
            cur = first
            k = 4
            print(cur, end="   ")
            while k <= 8:
                if str(cur)[2:] in begins[k] :
                    print( begins[k][str(cur)[2:]] , end="   ")
                    cur = begins[k][str(cur)[2:]][0]
                    k += 1
                else:
                    break
            print()

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
