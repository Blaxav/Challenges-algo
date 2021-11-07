import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime


if __name__ == '__main__' :
    start = time.time()

    res = []

    nbr = 1
    cnt = 1
    cPow = 0
    while cPow <= 6 :
        cnt += len(str(nbr))

        if cnt > 10**cPow:
            print("coucou ", 10**cPow, nbr, cnt)
            print("    ", str(nbr))
            res.append(str(nbr)[ - cnt + 10**cPow])
            print("    ", res)
            cPow +=1
        nbr += 1

        if cPow == 7:
            break
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))