import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime


if __name__ == '__main__' :
    start = time.time()

    perims = {}

    for a in range(1, 1000):
        for b in range(a, 1000):
            c = sqrt(a**2 + b**2)
            if int(c) == c and (a+c+b <= 1000 ):
                if (a+b+c) in perims :
                    perims[a+b+c] += 1
                else :
                    perims[a+b+c] = 1

    maxL = 0
    maxP = 0
    for k in perims:
        if perims[k] > maxL:
            maxL = perims[k]
            maxP = k
            print(k, perims[k])


    print("Result: ", k, perims[k])

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))