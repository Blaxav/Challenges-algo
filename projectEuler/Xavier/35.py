import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime

if __name__ == '__main__' :
    start = time.time()

    g = prime_numbers()
    pri = str(next(g))

    rota = set()
    cnt = 0
    pascool = False
    while int(pri) < 1e6:
        pascool = False
        #print(pri)
        for z in range(len(pri)):
            cVal = int(pri[z:] + pri[:z])
            #print("   ", cVal, is_prime(cVal))
            if is_prime(cVal) == False:
                pascool = True
                break
        if not pascool:
            print("Adding: ", pri)
            rota.add(pri)
        cnt += 1
        if cnt % 10000 == 0:
            print(cnt, pri, len(rota))
        pri = str(next(g))
        
    #print(rota)
    print("Result: ", len(rota))

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))