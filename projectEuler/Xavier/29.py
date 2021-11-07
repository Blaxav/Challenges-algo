import time
from utils import prime_numbers
from utils import add_one
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    maxPow = 100

    results = set()

    for a in range(2,maxPow+1):
        for b in range(2,maxPow+1):
            results.add(a**b)
    
    print(len(results))

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))