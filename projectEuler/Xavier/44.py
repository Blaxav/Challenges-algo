import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime

def pentag():
    i = 0
    while True:
        i += 1
        yield int(i*(3*i-1)/2)

def is_pentag(n):
    g = pentag()
    p = next(g)
    while p <= n:
        if p == n:
            return True
        p = next(g)
    return False

if __name__ == '__main__' :
    start = time.time()

    g = pentag()
    p1 = next(g)
    allP = [1]
    cnt = 0

    minDif = 10e6

    while p1 - allP[-1] < minDif:
        
        for p2 in allP[::-1]:
            if p1 - p2 > minDif :
                ind = allP.index(p2)
                allP = allP[ind:]
                break

            if abs(p2-p1) in allP:
                #print(p1, p2, abs(p1-p2), minDif)
                if is_pentag(p1+p2):
                    minDif = min([p1 - p2, minDif])
                    print( "    COUCOU : ", p2, p1, minDif)
                
        allP.append(p1)
        p1 = next(g)
        if cnt % 10000 == 0:
            print("%-15i%-15i%-15i%-15i%-15i" % (p1, allP[-1], p1 - allP[-1], minDif, minDif - (p1 - allP[-1]) ) )
        cnt += 1
    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))