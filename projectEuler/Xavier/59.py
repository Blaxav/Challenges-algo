import time
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)


def decrypt(codes, keys):
    n = len(keys)

    i = 0
    message = []
    Ok = True
    for code in codes:
        key = keys[i % n]
        message.append( chr(key^code) )
        if chr(key^code) < chr(20) or chr(key^code) > chr(122):
            message = []
            break
            
        i += 1
    
    return message

def print_message(list_codes, i, j, k):
    if len(list_codes) > 0:
        somme = 0
        print(chr(i), chr(j), chr(k))
        for car in list_codes:
            print(car, end="")
            somme += ord(car)
        print()
        print("Somme = ", somme)

if __name__ == '__main__' :
    start = time.time()

    inputFile = open("input_59.txt")
    for line in inputFile:
        codes = [int(i) for i in line.split(',')]
    

    minVal = ord('a')
    maxVal = ord('z')
    message = []
    for i,j,k in product( range(minVal, maxVal+1), repeat=3):
        message = decrypt(codes, [i,j,k])
        print_message(message, i, j, k)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
