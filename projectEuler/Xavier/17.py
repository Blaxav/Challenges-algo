import time
from math import sqrt

from utils import add_one, prime_numbers

smalls = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen","fifteen", "sixteen",
        "seveteen", "heighteen", "nineteen"]
meds = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
bigs = ["hundred", "thousand"]

def convert(i):
    result = 0
    if i // 1000 > 0:
        result += len(smalls[i // 1000]) + len("thousand")
        print(smalls[i // 1000], " thousand", end=" ")
    i = i % 1000
    if i // 100 > 0:
        result += len(smalls[i // 100]) + len("hundred")
        print(smalls[i // 100], " hundred", end=" ")
        
        i = i % 100
        if i > 0:
            result += len("and")
            print( "and ", end=" ")

    if i > 0:
        if i < 20 :
            result += len(smalls[i])
            print(smalls[i], end=" ")
        else :
            result += len(meds[i // 10])
            print(meds[i // 10], end=" ")
            i = i % 10
            if i > 0:
                print(smalls[i], end=" ")
                result += len(smalls[i])
    
    return result

if __name__ == '__main__' :
    start = time.time()

    
    N = 1001
    total = 0
    cur = 0
    for i in range(1,N):
        cur = convert(i)
        total += cur
        print(cur, total)

    print("Result: ", total)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
