import time
from utils import prime_numbers
from utils import add_one
from math import sqrt

def is_prime(n):
    g = prime_numbers()
    pri = next(g)
    while pri <= n:
        if pri == n:
            return True
        pri = next(g)
    return False

def quad(n,a,b):
    return (n**2) + (a*n) + b

if __name__ == '__main__' :
    start = time.time()

    g = prime_numbers()
    b = next(g)
    Nmax = 1000

    primes = []
    while b < Nmax:
        b = next(g)
        primes.append(b)
    primes.sort(reverse=True)

    max_len = 0
    max_a = 0
    max_b = 0
    
    for b in primes:
        for i in [-1,1]:
            for xi in primes:
                a = xi - b - 1
                
                n = 0
                while is_prime(quad(n,a,i*b)):
                    n += 1
                
                if n > max_len:
                    max_len = n
                    max_a = a
                    max_b = i*b
        print("%-10i%-10i%-10i%-10i%-10i%-10i" %(i*b, a, n, max_a, max_b, max_len))
    
    print("Max len: ", max_len)
    print("a:       ", max_a)
    print("b:       ", max_b)
    print("Result:  ", max_a*max_b)
        




    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))