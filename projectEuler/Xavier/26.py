import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from decimal import Decimal


def division(a):
    divs = []
    cur = 10
    result = []

    while True:
        if (cur // a) in divs:
            for divisor in divs[divs.index(cur//a):]:
                for num in str(divisor):
                    result.append(num)
            return len(result)
        else:
            divs.append(cur//a)
            cur = 10**(len(str(a))) * (cur % a)
        
        if cur == 0:
            return 0

if __name__ == '__main__' :
    start = time.time()
    
    max_len     = 0
    cur_len     = 0
    best_id     = 0

    N = 10000

    for i in range(1, N):
        cur_len = division(i)

        if cur_len > max_len:
            max_len = cur_len
            best_id = i
            

    print("best id: ", best_id)
    print("Max len: ", max_len)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))