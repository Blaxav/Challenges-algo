import time
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    n1 = 2
    n2 = 6
    i = 1
    while True:
        sol = set()
        for k in range(n1,n2+1):
            #print( "".join( sorted(str(k*i) )  ) )
            sol.add( "".join( sorted(str(k*i) )  ) )
        if len(sol) == 1:
            print("Result: ", i)
            for k in range(n1, n2 + 1):
                print("         ", k*i, "".join( sorted(str(k*i) )) )
            break
        
        if i % 10000000 ==0:
            print(i)
        i += 1

    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
