import time
from utils import prime_numbers
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    N = 10001
    gen = prime_numbers()
    for i in range(N-1):
        next(gen)
    print(next(gen))

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))