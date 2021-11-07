import time
from utils import prime_numbers
from utils import add_one
from math import sqrt

def divs(n):
    if n == 1:
        return [1]
    else:
        l = [1]
        div = 2
        endVal = int(n/2)
        while div <= endVal:
            if n % div == 0:
                l.append(div)
                if div != n // div:
                    l.append(n // div)
            div += 1
            endVal = int(n/div)
    return l

if __name__ == '__main__' :
    start = time.time()

    N = 28123

    l = [i for i in range(1, N)]

    # 1 on cherche les abondants
    abondants = []
    for i in range(1, N):
        # si i est abondant
        if sum(divs(i)) > i:
            abondants.append(i)
    
    cnt = 0
    for i in range(len(abondants)):
        for j in range(i, len(abondants)):
            if abondants[i] + abondants[j] < 28200 :
                if abondants[i] + abondants[j] in l:
                    l.remove( abondants[i] + abondants[j] )
            #print(abondants[i] + abondants[j], l)
        
            cnt += 1
            if cnt % 100000 == 0:
                print(i, len(l))
        

    print( "Result: ", sum(l) )

    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))