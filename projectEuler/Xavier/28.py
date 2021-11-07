import time
from utils import prime_numbers
from utils import add_one
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    current = 1
    length = 2
    total = 1

    maxSize = 1000

    while length <= maxSize:
        for i in range(4):
            current += length
            total += current
            #print("%-10i%-10i" % (current, total))
        length += 2
    
    print("Result: ", total)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))