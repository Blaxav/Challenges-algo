from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        arrivalTime, busList = f.readlines()
        arrivalTime = int(arrivalTime.strip())        
        busList = busList.split(',')
        return arrivalTime, busList

def findGapBetweenTwoMaxes(maxes: list, gaps: list):
    coeffs, found = {k:1 for k in range(len(maxes))}, 0
    while True:
        if maxes[0]*coeffs[0] - maxes[1]*coeffs[1] == gaps[0] - gaps[1]:
            conditions = [((maxes[0]*coeffs[0] - gaps[0] + gaps[it]) % maxes[it] == 0) for it in range(2,len(maxes))]
            if False not in conditions:
                found += 1
                for it in range(2,len(maxes)):
                    coeffs[it] = (maxes[0]*coeffs[0] - gaps[0] + gaps[it]) // maxes[it] + 1         
                if found == 1:
                    found1 = maxes[0]*coeffs[0]
                if found == 2:
                    return maxes[0]*coeffs[0] - found1, found1
            coeffs[0] += 1
            coeffs[1] += 1
        elif maxes[0]*coeffs[0] - maxes[1]*coeffs[1] > gaps[0] - gaps[1]:
            coeffs[1] += 1 
        else:
            coeffs[0] += 1

            
def part1(arrivalTime: int, busList: list):
    offset = 0
    while True:
        for bus in busList:
            if (arrivalTime + offset) % bus == 0:               
                return bus * offset
        offset += 1

def part2(busList: list):
    orderBusDict = {int(v):k for k, v in enumerate(busList) if v.isdigit()}
    sortedBusIds = sorted(orderBusDict.keys(), reverse=True)
    init = 4
    maxes = sortedBusIds[:init]
    gaps = [orderBusDict[elem] for elem in maxes]
    gaps[0] = orderBusDict[maxes[0]]
    it, start = findGapBetweenTwoMaxes(maxes, gaps)
    for elem in maxes:
        del orderBusDict[elem]

    res = False
    while not res:
        for busId in orderBusDict:
            if (start - gaps[0] + orderBusDict[busId]) % busId == 0:
                res = True
            else:
                res = False
                break
        if res:
            return start - gaps[0]
        else:
            start += it


class Tests(unittest.TestCase):

    def testP2(self):
        self.assertEqual(part2(['1789','37','47','1889']), 1202161486)


if __name__ == "__main__":
    # unittest.main()
    arrivalTime, busList = readFile()
    p1 = part1(arrivalTime, [int(i) for i in busList if i.isdigit()])
    print(f"Part 1: {p1}")
    p2 = part2(busList)
    print(f"Part 2: {p2}")
    print(time()-a)

