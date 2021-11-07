import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime

def add(l, g):
    for i in range(len(g)):
        if i >= len(l):
            l.append(0)
        l[i] += g[i]

        cInd = i
        while l[cInd] >= 10:
            if cInd + 1 == len(l):
                l.append(0)
            l[cInd+1] += l[cInd] // 10
            l[cInd] = int(str(l[cInd])[-1])


if __name__ == '__main__' :
    start = time.time()

    N = 1000

    somme = [0]
    for i in range(1, N+1):
        cVal = [int(e) for e in str(i**i)][::-1][:10]
        add(somme, cVal)


    print(somme[::-1])

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))