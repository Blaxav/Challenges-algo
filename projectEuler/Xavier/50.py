import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime


if __name__ == '__main__' :
    start = time.time()

    N = 1000000

    g = prime_numbers()
    init = next(g)
    
    sols = []

    initM = 0
    cntM = 0
    sommeM = 0

    while init < N:
        g2 = prime_numbers()
        p = next(g2)
        while p < init:
            p = next(g2)
        somme = p
        cnt = 1
        while somme < N:
            p = next(g2)
            somme += p
            cnt += 1
            if is_prime(somme):
                if cnt > cntM:
                    cntM = cnt
                    initM = init
                    sommeM = somme

                    print("%-15i%-15i%-15i" % (init, cnt, somme ) )
        
        init = next(g)


    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))