import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime

ALPHA = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__ == '__main__' :
    start = time.time()

    maxSize = 0
    inputFile = open("input_42.txt")
    words = inputFile.readlines()[0].split(",")
    words = [w[1:-1] for w in words]

    print("N words: ", len(words))
    maxLen = 0
    for w in words:
        if len(w) > maxLen:
            maxLen = len(w)
    print("Max len of a words :", maxLen)
    
    maxVal = 16*26
    print("Max val of the sum of the letters code :", maxVal)


    triangles = []
    cVal = 0
    cInd = 0
    while cVal < maxVal:
        cInd += 1
        cVal = int(cInd*(cInd+1)/2)
        triangles.append(cVal)
    
    print("Possible triangles values: ", triangles)

    cnt = 0
    for w in words:
        cVal = sum( [ALPHA.index(e) for e in w] )
        if cVal in triangles:
            cnt += 1

    print("Result: ", cnt)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))