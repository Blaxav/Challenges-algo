from itertools import takewhile
from math import sqrt


def prime_numbers():
    yield 2
    i = 3
    prime = [2]
    while True:
        if all( (i % j != 0 for j in takewhile(lambda x: x <= sqrt(i), prime) ) ) :
            prime.append(i)
            yield i
        i+= 2

def is_prime(n):
    if n < 2:
        return False
        
    cDiv = 2
    while cDiv <= sqrt(n):
        if n % cDiv == 0:
            return False
        cDiv += 1
    return True

def prime_factors(n):
    gen = prime_numbers()
    cnt_local = 0
    cnt_total = 0
    div = next(gen)
    Stop = n
    while div <= Stop:
        cnt_local = 0
        while n % div == 0:
            n /= div
            cnt_local += 1
        if cnt_local > 0:
            yield (div, cnt_local)
        cnt_total += cnt_local
        div = next(gen)
    # Si cnt == 0 , aucun facteur premier trouvé, n est premier
    # on revoie n
    if cnt_total == 0:
        yield n


"""
Name :  add_one
Brief: add one to a list with a basis on each element defined by 
        an other list a max values
Params :
    l: list on which add one
    maxValue: list of size len(l) defining the max value of l[i] (maxValue excluded)
Return Value:
    If succed to add one: return True
    If not, returns False, besause the max value allowed by this representation
        has been reached
        Example: l = [1, 1, 1], maxValue = [2, 2, 2] -> l is already the max of this
            representation
Examples:
    l           = [0, 1, 5 ,2]
    maxValue    = [3, 2, 6, 8]

    add_one(l, maxValue) = [1, 1, 5, 2]
    add_one(l, maxValue) = [2, 1, 5, 2]
    add_one(l, maxValue) = [0, 0, 0, 3]
"""
def add_one(l,maxValues):
    ind = 0
    l[ind] += 1
    while l[ind] == maxValues[ind]:
        ind += 1
        if ind == len(l):
            return False
        l[ind] += 1
    for i in range(ind):
        l[i] = 0
    return True

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

def propagate_left_to_right(l):
    ind = 0
    maxInd = len(l) - 1
    while ind <= maxInd:
        if l[ind] >= 10 :
            if ind >= len(l) - 1 :
                l.append(0)
                maxInd += 1

            l[ind + 1] += l[ind] // 10
            l[ind] = int(str(l[ind])[-1])

        ind += 1

def list_to_nbr(l):
    return "".join( [str(i) for i in l] )[::-1]
