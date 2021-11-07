import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime
from utils import prime_factors


if __name__ == '__main__' :
    start = time.time()

    N = 1000000
    allNbr = [0 for i in range(N)]

    g = prime_numbers()
    p = next(g)
    while p < (N/2):

        k = 1
        while k*p < N:
            allNbr[k*p] += 1
            k += 1
        p = next(g)

    cnt = 0
    voulu = 4

    for i in range(N):
        
        if allNbr[i] == voulu:
            cnt += 1
        else :
            cnt = 0

        if cnt == voulu :
            break

    print("Result: ", i - cnt + 1)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))