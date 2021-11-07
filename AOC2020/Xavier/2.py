import time
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    fileIn = open("in_02.txt")
    valid = 0
    
    for line in fileIn:
        rng, letter, pw = line.split()

        rng = [int(i) for i in rng.split("-")]
        letter = letter[:-1]

        cnt = 0
        for pos in rng:
            if pw[pos-1] == letter:
                cnt += 1
                if cnt == 2:
                    break
        
        if cnt == 1:
            valid += 1 

    print("Result: ", valid)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
