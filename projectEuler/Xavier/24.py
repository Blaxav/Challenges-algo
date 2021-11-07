import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from functools import lru_cache

@lru_cache(maxsize = None)
def n_permuts(n):
    if n == 1:
        return 1
    else :
        return n * n_permuts(n-1)


if __name__ == '__main__' :
    start = time.time()

    N = int(1e6) - 1
    nMax = 10

    l = [i for i in range(nMax)]

    
    final = []
    cSize = nMax


    while cSize > 1 :
        inner_permuts = n_permuts(cSize - 1)
        elem = N // inner_permuts
        #print()
        #print("N: ",N)
        #print("innerperm: ", inner_permuts)
        #print("div: ", elem)
        final.append( l[elem] )
        del l[elem]
        N -= elem * inner_permuts
        cSize -= 1
        #print(final, l)

    final.append(l[0])

    for i in final:
        print(i, end="")


    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))