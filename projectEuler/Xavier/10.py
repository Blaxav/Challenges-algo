import time
from utils import prime_numbers
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    gen = prime_numbers()
    N = 2000000
    p = next(gen)
    sumPrims = 0
    while p < N:
        sumPrims += p
        p = next(gen)

    print("Result: ", sumPrims)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))