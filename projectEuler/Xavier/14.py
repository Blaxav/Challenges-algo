import time
from utils import prime_numbers
from math import sqrt

def next_syracuse(i):
    if i % 2 == 0:
        return int(i/2)
    else :
        return 3*i + 1 

def iter_to_one(u0):
    cnt = 1
    while u0 != 1:
        cnt += 1
        u0 = next_syracuse(u0)
    return cnt

if __name__ == '__main__' :
    start = time.time()

    N = int(1e6)
    umax = 0
    longueur = 0
    lmax = 0
    for i in range(1, N+1):
        longueur = iter_to_one(i)
        if longueur > lmax:
            umax = i
            lmax= longueur
            print("%-10i%-10i" % (i , longueur) )


    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))