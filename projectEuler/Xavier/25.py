import time
from utils import prime_numbers
from utils import add_one
from math import sqrt

def sizeof(n):
    return len(str(n))

if __name__ == '__main__' :
    start = time.time()

    i = 3
    previous = 2
    ante = 1
    current = 3
    logite = 10
    print(1)
    print(2)
    print(3)

    cnt = 4
    while sizeof(current) < 1000:
        ante = previous
        previous = current
        current = previous + ante
        #print(current)
        cnt += 1


    print("Result! ", cnt)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))