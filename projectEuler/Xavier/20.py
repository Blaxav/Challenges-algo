import time
from math import sqrt

from utils import add_one, prime_numbers


def expand(n,l):
    for i in range(len(l)):
        l[i] *= n

    need = True
    while need:
        need = False
        for i in range(len(l)):
            if l[i] >= 10 :
                if i == len(l) - 1 :
                    l.append(0)
                    need =True
                l[i+1] += l[i] // 10
                l[i] = l[i] % 10


if __name__ == '__main__' :
    start = time.time()

    nbr = [1]
    for i in range(1,100):
        expand(i, nbr)
        print(nbr)
    
    print("Result: ", sum(nbr))
        

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
