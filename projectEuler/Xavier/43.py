import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime
from itertools import permutations


if __name__ == '__main__' :
    start = time.time()

    pos5 = [0, 5]
    pos4 = [0, 2, 4, 6, 8]

    pos345 = []
    for a in range(10):
        for b in range(a+1,10):
            for c in range(b+1,10):
                if (a+b+c) % 3 == 0 :
                    pos345.append([a,b,c])

    print(pos345)

    cnt = 0
    allN = []
    for (a,b,c) in pos345:
        for (a3, a4, a5) in permutations([a,b,c]):
            if a4 in pos4:
                for a6 in [ i for i in [0,5] if i not in [a3, a4, a5]]:
                    #print(a3, a4, a5, a6)
                    remain = [i for i in range(10) if i not in [a3, a4, a5, a6]]
                    for (a1, a2, a7, a8, a9, a10) in permutations(remain) :
                        if int(str(a5) + str(a6) + str(a7) ) % 7 == 0:
                            if int(str(a6) + str(a7) + str(a8) ) % 11 == 0:
                                if int(str(a7) + str(a8) + str(a9) ) % 13 == 0:
                                    if int(str(a8) + str(a9) + str(a10) ) % 17 == 0:
                                        print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
                                        allN.append( int( str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6) + str(a7) + str(a8) + str(a9) + str(a10) ) )
                                        print(allN[-1])
    print(cnt)

    print(sum(allN))
                    
    
    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))