import time
from utils import prime_numbers
from utils import add_one
from math import sqrt


def factorial(n):
    result = 1
    for k in range(n, 0, -1):
        result *= k
    return result

if __name__ == '__main__' :
    start = time.time()

    #check stop
    iMax = 1
    while 10**iMax <= iMax * factorial(9):
        iMax += 1
    print("Couou ", iMax)
    
    allOk = []
    for i in range(3, 10**iMax):
        digits = [int(e) for e in str(i)]
        #print(i, digits, [factorial(z) for z in digits], sum([factorial(z) for z in digits]))
        if sum([factorial(z) for z in digits]) == i:
            allOk.append(i)
        if i % 100000 == 0:
            print(i, allOk)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))