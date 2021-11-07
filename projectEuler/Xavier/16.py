import time
from utils import prime_numbers
from math import sqrt


if __name__ == '__main__' :
    start = time.time()

    l = [1]
    power = 1000
    for i in range(power):
        l = [2*i for i in l]
        for i in range(len(l)):
            if l[i] >= 10:
                if i+1 == len(l):
                    l.append(0)
                l[i+1] += 1
                l[i] -= 10
        #print(l)
    print("Result: ", sum(l))

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))