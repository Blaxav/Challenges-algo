import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime
from itertools import permutations

if __name__ == '__main__' :
    start = time.time()

    cSize = 2
    maxPrime = 0
    while cSize < 10:
        cList = [str(i) for i in range(1, cSize + 1)]
        for cl in permutations(cList):
            cStr = ""
            for k in cl:
                cStr += k
            cNum = int(cStr)
            if is_prime(cNum):
                maxPrime = cNum
        cSize += 1
    
    print("Result ", maxPrime)


    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))