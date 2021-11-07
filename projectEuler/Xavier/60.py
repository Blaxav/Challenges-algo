import time
from collections import defaultdict
#from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)


def rel(p,q):
    if is_prime( int( str(p) + str(q) )) and\
            is_prime( int( str(q) + str(p) )):
        return True
    return  False

def bourrin():

    g = prime_numbers()
    primes = []
    voisins = defaultdict(lambda: set() )
    p = 1
    found = False

    while not found :
        #1. on ajoute un premier et ses voisins
        p = next(g)
        for q in primes:
            if rel(p,q):
                voisins[p].add(q)
                #voisins[q].add(p)

        primes.append(p)

        #2. on cherche les gens en relations a plusieurs incluant p
        for v1 in voisins[p]:
            cand2 = [i for i in voisins[p] if i in voisins[v1]]
            for v2 in cand2:
                cand3 = [i for i in cand2 if i in voisins[v2]]
                for v3 in cand3:
                    print("potential: ", p, v1, v2, v3)
                    cand4 = [i for i in cand3 if i in voisins[v3]]
                    for v4 in cand4:
                        print("Found: ", p, v1, v2, v3, v4)
                        print("Result:", sum([p, v1, v2, v3, v4]))
                        found = True




if __name__ == '__main__' :

    start = time.time()

    bourrin()
    

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
