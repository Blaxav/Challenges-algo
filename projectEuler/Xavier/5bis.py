import time
from utils import prime_numbers
from utils import prime_factors
from math import sqrt
from collections import defaultdict

if __name__ == '__main__' :
    start = time.time()

    N = 2000
    result = 1
    dico_factors = defaultdict(lambda: 1)
    cnt = 0

    g = prime_numbers()
    prime = next(g)
    power = 1
    while prime <= N :
        power = 1
        while prime**(power + 1) <= N:
            power += 1
        result *= prime**power
        prime = next(g)

    print("Result: ", result)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))

   