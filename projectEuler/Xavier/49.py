import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime
from collections import defaultdict

if __name__ == '__main__' :
    start = time.time()

    g = prime_numbers()
    p = next(g)

    while p < 1000:
        p =     next(g)
    
    primes4Digits = [p]
    while p < 10000:
        p = next(g)
        primes4Digits.append(p)

    print("List size: ", len(primes4Digits))

    # on recupere ceux qui apparaissent trois fois en string trié
    words = defaultdict(lambda: [])

    for prime in primes4Digits:
        w = ''.join( sorted(str(prime)))
        words[ w ].append(prime)

    diffMatrix = []
    for w in words:
        diffMatrix = []
        sW = len(words[w])
        if sW >= 3:
            occurences = defaultdict(lambda: 0)
            for i in range(sW-1):
                for j in range(i+1, sW):
                    step = words[w][j] - words[w][i]
                    
                    if words[w][j] + step in words[w]:
                        print( "Trouve: ", words[w][i],words[w][j],words[w][j] + step)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))