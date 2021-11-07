import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime


if __name__ == '__main__' :
    start = time.time()

    truncables = set()
    g = prime_numbers()


    cnt = 0
    trunc = True
    while len(truncables) < 11:
        prime = str(next(g))
        trunc = True

        for z in range(len(prime)):
            #print(prime, prime[:z], prime[z:])
            if len(prime[:z]) > 0 and not is_prime(int(prime[:z])):
                trunc = False
                break
            if len(prime[z:]) > 0 and not is_prime(int(prime[z:])):
                trunc = False
                break
        if trunc:
            if int(prime) >= 10:
                truncables.add( int(prime) )
                #print(truncables)
        cnt += 1
        if cnt % 10000 == 0:
            print(cnt, len(truncables), prime)

    print(truncables)
    print("Result: ", sum(truncables))
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))