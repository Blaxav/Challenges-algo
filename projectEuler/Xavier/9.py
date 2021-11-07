import time
from utils import prime_numbers
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    for a in range(1, 1000):
        for b in range(1,1000-a):
            c = 1000 - (a + b )
            if c**2 == a**2 + b**2 :
                print("coucou", a, "   ", b, "   ", 1000-(a+b))
                print("   prod: ", a*c*b)

    print("Result: ", a,b)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))