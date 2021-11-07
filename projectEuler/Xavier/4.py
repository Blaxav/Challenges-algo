import time
from utils import prime_numbers
from math import sqrt

def is_palyndrom(mot) :
    n = len(mot)
    i = 0
    while i < n - i - 1:
        if mot[i] != mot[n - i - 1] :
            return False 
        i += 1
    return True


if __name__ == '__main__' :
    start = time.time()

    maxpal = 0
    n_digits = 3
    for i in range(10**n_digits):
        for j in range(i, 10**n_digits):
            if is_palyndrom( str(i*j)) :
                #   print(maxpal, i*j)
                maxpal = max(maxpal, i*j)
                #print(i*j)

    print(maxpal)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))