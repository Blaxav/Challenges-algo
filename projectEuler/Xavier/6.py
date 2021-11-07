import time
from utils import prime_numbers
from math import sqrt
from sys import argv

if __name__ == '__main__' :
    start = time.time()

    N = int(argv[1])
    sumSq = 0
    sumN = 0
    for i in range(1,N+1):
        sumN += i
        sumSq += i**2
    
    print(sumN**2 - sumSq)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))