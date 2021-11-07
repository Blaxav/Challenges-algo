import time
from itertools import combinations
from math import sqrt

from utils import add_one, is_prime, prime_numbers


def ex1():
    nbrsFile = open("in_01.txt")

    nbrs = []
    n = 0
    for line in nbrsFile :
        cur = int(line)

        for i in range(n):
            if nbrs[i] + cur < 2020:
                for j in range(i+1, n):
                    if  nbrs[i] + cur + nbrs[j] == 2020:
                        print("Found ",  nbrs[i], nbrs[j], cur ,nbrs[i]*nbrs[j]*cur)
                        return 0
        n += 1
        nbrs.append(cur)

if __name__ == '__main__' :
    start = time.time()

    ex1()

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
