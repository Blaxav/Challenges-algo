import math
import sys
from datetime import date, datetime
from functools import lru_cache


@lru_cache(maxsize=None)
def divs_cache(n):
    if n == 1:
        return [1]
    else:
        l = [1, n]
        div = int(n/2) + 1
        endVal = 1
        while div >= endVal:
            if n % div == 0:
                l += divs(div)
                # for d in divs(div):
                #    l.add(int(n/d))

                endVal = max(divs(div))
                # print(n, " ", div, " ", divs(div),
                #      " ", l, "   endval = ", endVal)
            div -= 1

    return list(set(l))


def divs(n):
    if n == 1:
        return [1]
    else:
        l = [1, n]
        if n == n // math.sqrt(n):
            l.append(int(math.sqrt(n)))
        div = 2
        endVal = int(math.sqrt(n)) - 1
        while div <= endVal:
            if n % div == 0:
                l.append(div)
                l.append(n / div)
            div += 1
            endVal = int(n/div)
    return l


def GetDivisors(n):
    small_divisors = [i for i in range(
        1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors


if __name__ == '__main__':

    n = 1
    timer = datetime.now()
    print("Target : ", int(int(sys.argv[1]) / 10))
    while sum(GetDivisors(n)) < int(int(sys.argv[1]) / 10):
        n += 1
        if n % 100000 == 0:
            print(n)

    print("Time divisors by array: ", datetime.now() - timer)
    print("Part 1: ", n)

    n = 1
    timer = datetime.now()
    print()
    while sum(divs(n)) < int(int(sys.argv[1]) / 10):
        n += 1
        if n % 100000 == 0:
            print(n)

    print("Time divisors by forloop: ", datetime.now() - timer)
    print("Part 1: ", n)
    exit()
    presents = int(sys.argv[1])

    houses = [0] * (presents + 1)
    lutin = 1
    house_min = 1
    max_val = 0
    min_house = presents
    while lutin < min_house:
        for k in range(1, 51):
            if k*lutin <= presents:
                houses[k*lutin] += 11*lutin
                if houses[k*lutin] > max_val:
                    max_val = houses[k*lutin]
                    if max_val >= int(sys.argv[1]):
                        #print("Part 2 :", k*lutin)
                        if k*lutin < min_house:
                            min_house = k*lutin
        if lutin % 100000 == 0:
            print("%-15i%-15i%-15i" % (lutin, max_val, min_house))
        lutin += 1
