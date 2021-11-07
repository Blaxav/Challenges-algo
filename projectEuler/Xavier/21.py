import time
from math import sqrt

from utils import add_one, prime_numbers


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

def sumNbrs(n):
    strNbr = str(n)
    res = 0
    for i in strNbr:
        res += int(i)
    return res

if __name__ == '__main__' :
    start = time.time()

    amicable = set()
    sumDict = {}
    for i in range(1, 10001):
        sumDict[i] = sum(divs(i))
        
        for v in range(2,i):
            if sumDict[i] == v and sumDict[v] == i:
                if i != v :
                    amicable.add(i)
                    amicable.add(v)
                    print(i, sumDict[i], divs(i))
                    print(v, sumDict[v], divs(v))
                    print()
                    #if len(amicable) % 1000 == 0:
                    #    print(i,v)
    res = 0
    print(amicable)
    for i in amicable:
        res += i
    
    print("Result: ", res)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
