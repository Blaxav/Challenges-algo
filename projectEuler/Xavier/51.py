import time
from collections import defaultdict
from itertools import combinations
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    N = 8

    g = prime_numbers()
    p = next(g)

    found = False
    primesG = []

    while not found:
        digits = defaultdict(lambda: [])
        place = 0
        for d in str(p):
            digits[d].append(place)
            place += 1

        for d in digits:
            for k in range(len(digits[d])):
                for comb in combinations(digits[d], k + 1):
                    stop = 0
                    found = True
                    primesG.clear()

                    newNbr = list( str(p) )
                    for rplct in "0123456789" :
                        for ind in comb:
                            newNbr[ind] = rplct
                        if not is_prime( int( "".join( newNbr ) ) ):
                            stop += 1
                            if stop == (10 - N  + 1 ) :
                                found = False
                        elif "".join( newNbr )[0] == "0":
                            stop += 1
                            if stop == (10 - N  + 1 ) :
                                found = False
                        else:
                            primesG.append( int( "".join( newNbr ) ) )
                    
                    if found:
                        print("Found: ", p, primesG)
                        break
                if found:
                    break
            if found:
                break
        if found:
            break

        p = next(g)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
