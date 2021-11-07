import time
from utils import prime_numbers
from utils import add_one
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    log = 1000
    cnt = 0 

    pandigits = set()
    for a in range(1, 10000):
        maxPow = 5 - len(str(a))
        for b in range(a, 10**maxPow):
            if len(str(a)) + len(str(b)) + len(str(a*b)) == 9:
                cnt += 1
                concat = str(a) + str(b) + str(a*b)
                if sorted(concat) == [str(i) for i in range(1,10)] :
                    pandigits.add(a*b)
        if a % log == 0:
            print(a, cnt, len(pandigits))
    print("Result: ", sum(pandigits))

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))