import time
from utils import prime_numbers
from utils import add_one
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    cPow = 5
    i = 2

    okNumbers = []

    while i < 10000000:
        cTot = 0
        for e in str(i):
            cTot += int(e)**cPow
        if cTot == i :
            okNumbers.append(i)
        i += 1
    
    print(okNumbers)
    print("Result: ", sum(okNumbers))

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))