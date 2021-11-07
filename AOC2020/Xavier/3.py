import time
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    fileIn = open("input_3.txt")
    rows = []
    for line in fileIn:
        rows.append(line.rstrip('\n'))

    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    
    height = len(rows)
    width = len(rows[0])
    print("H: ", height)
    print("W: ", width)
    curPos = [0,0]

    totMoovesList = []
    sapinsList = []
    for slope in slopes:
        totMooves = 0
        sapins = 0
        curPos = [0,0]

        while curPos[1] + slope[1] < height:
            curPos[1] += slope[1]
            curPos[0] = (curPos[0] + slope[0]) % width
            
            if rows[curPos[1]][curPos[0]] == '#':
                sapins += 1
            totMooves += 1
        
        print("Tot mooves: ", totMooves)
        print("Sapins:     ", sapins)
        print()
        totMoovesList.append(totMooves)
        sapinsList.append(sapins)

    product = 1
    for sap in sapinsList:
        product *= sap

    print("Result: ", product)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
