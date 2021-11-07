import time
from itertools import takewhile
from math import sqrt

def prime_numbers_all():
    i = 2
    prime = []
    while True:
        if all( (i % j != 0 for j in prime) ) :
            prime.append(i)
            yield i
        i+= 1

def prime_numbers_any():
    i = 2
    prime = []
    while True:
        if any( (i % j == 0 for j in prime) ) :
            pass
        else:
            prime.append(i)
            yield i
        i+= 1

def prime_numbers_all_sqrt():
    i = 2
    prime = []
    while True:
        if all( (i % j != 0 for j in takewhile(lambda x: x <= sqrt(i), prime) ) ) :
            prime.append(i)
            yield i
        i+= 1

def prime_numbers_all_sqrt_2():
    i = 3
    prime = [2]
    while True:
        if all( (i % j != 0 for j in takewhile(lambda x: x <= sqrt(i), prime) ) ) :
            prime.append(i)
            yield i
        i+= 2

def prime_numbers_all_2():
    i = 3
    prime = [2]
    while True:
        if all( (i % j != 0 for j in prime) ) :
            prime.append(i)
            yield i
        i+= 2

def prime_numbers_any_2():
    i = 3
    prime = [2]
    while True:
        if any( (i % j == 0 for j in prime) ) :
            pass
        else:
            prime.append(i)
            yield i
        i+= 2

def eratostene(n):
    candidates = range(2,n+1)

    for i in range(n+1):
        yield candidates[0]
        candidates = [j for j in candidates[1:] if j % candidates[0] != 0]
        

def test_gen(N, genToTry):
    start = time.time()

    g = genToTry()
    for i in range(N):
        next(g)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))

#######################################################################################
#                   TEST OF DIFFERENT GENS
#######################################################################################
if __name__ == '__main__' : 

    N = 100000

    print("\nGen : SQRT")
    test_gen(N, prime_numbers_all_sqrt)


    print("\nGen : SQRT by 2")
    test_gen(N, prime_numbers_all_sqrt_2)

    
    exit()
    print("\nGen : ERATOSTENE 100 000")
    start = time.time()
    g = eratostene(700000)
    for i in range(N):
        next(g)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))

    print("\nGen : ERATOSTENE 700 000")
    start = time.time()
    g = eratostene(700000)
    for i in range(N):
        next(g)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))

    print("Gen : all")
    test_gen(N, prime_numbers_all)

    