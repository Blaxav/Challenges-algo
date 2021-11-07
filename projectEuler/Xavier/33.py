import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import divs


if __name__ == '__main__' :
    start = time.time()

    adiv = []
    bdiv = []

    division = []


    prods = []

    for a in range(10, 100):
        for b in range(10, 100):
            
            if a % 10 != 0 and b % 10 != 0:

                ########################################
                # 1. classical division
                division.clear()
                adiv = divs(a) + [a]
                bdiv = divs(b) + [b]
                intersect = [i for i in adiv if i in bdiv]
                intersect.sort(reverse=True)
                division.append(a/intersect[0])
                division.append(b/intersect[0])

                ########################################
                # 2. dumb division
                sa = str(a)
                sb = str(b)
                intersect = [i for i in sa if i in sb]
                da = [i for i in sa if i not in intersect]
                db = [i for i in sb if i not in intersect]
                if len(da) == 1 and len(db) == 1 :
                    if division[0] / division[1] == int(da[0]) / int(db[0]):
                        if a/b < 1.0:
                            print(sa, sb)
                            prods.append([a,b])
    
    num = 1
    denom = 1
    for i in prods :
        num *= i[0]
        denom *= i[1]
    
    numdiv      = divs(num) + [num]
    denomdiv    = divs(denom) + [denom]
    intersect = [i for i in numdiv if i in denomdiv]

    print(num)
    print(denom)
    print(intersect)
    intersect.sort(reverse=True)
    print(intersect[0])

    print()
    print("Result : ", num / intersect[0])

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))