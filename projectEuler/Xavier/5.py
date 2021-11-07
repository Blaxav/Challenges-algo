import time
from utils import prime_numbers
from utils import prime_factors
from math import sqrt
from collections import defaultdict

if __name__ == '__main__' :
    start = time.time()

    N = 2000
    result = 1
    dico_factors = defaultdict(lambda: 1)
    cnt = 0

    for i in range(2,N+1):
        #print(i)
        for e in prime_factors(i):
            #print("     ", e, end=" ")
            dico_factors[e[0]] = max([dico_factors[e[0]], e[1]])
        #print(i, dico_factors)

    for key in dico_factors:
        result *= key**dico_factors[key]
    print("Result: ", result)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))

   