import time
from utils import prime_numbers
from utils import add_one
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    pals = []
    for z in range(int(1e6)):
        if str(z) == str(z)[::-1]:
            if bin(z)[2:] == bin(z)[2:][::-1]:
                print(z)
                pals.append(z)
    
    print(len(pals))
    print("Result: ", sum(pals))
            
    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))