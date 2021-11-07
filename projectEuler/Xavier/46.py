import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime


if __name__ == '__main__' :
    start = time.time()

    n = 9
    while True:
        g = prime_numbers()
        p = next(g)
        isOk = False
        while p < n :
            if int(sqrt((n-p)/2)) == sqrt((n-p)/2):
                isOk = True
                #print(n, p , (n-p)/2 )
                break
            p = next(g)


        if not isOk:
            print("Found: ", n)
            break

        n+= 2
        while is_prime(n):
            n+=2

        if (n + 1) % 100000 == 0:
            print("%-10i" % n)
        

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))