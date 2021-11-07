import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    fileIn = open(sys.argv[1])

    for line in fileIn:
        for letter in "".join( re.findall('\w*(?=-)', line) ) :
            print(letter, end="")
        print()
        
    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
