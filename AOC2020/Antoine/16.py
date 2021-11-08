from time import time
import re
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines() if i.strip()]

def parseScheme(scheme: list):
    precisionRanges, nextIsYours, nextIsNearby, nearbyTickets = dict(), False, False, list()
    for instruction in scheme:
        if "your" in instruction:
            nextIsYours = True
        elif nextIsYours:
            yourTicket = [int(elem) for elem in instruction.split(',')]
            nextIsYours = False
        elif "nearby" in instruction:
            nextIsNearby = True
        elif nextIsNearby:
            nearbyTickets.append([int(elem) for elem in instruction.split(',')])
        else:
            precision, firstLowerBound, firstUpperBound, secondLowerBound, secondUpperBound = re.split(': |-| or ', instruction)
            precisionRanges[precision] = [range(int(firstLowerBound), int(firstUpperBound) + 1), range(int(secondLowerBound),int(secondUpperBound) + 1)]
    
    return precisionRanges, yourTicket, nearbyTickets

def part1(scheme: list):
    precisionRanges, yourTicket, nearbyTickets = parseScheme(scheme)
    errorRate, invalidTickets = 0, list()
    for nearbyTicket in nearbyTickets:
        for value in nearbyTicket:
            inPrecisionRange = False
            for precisionRange in precisionRanges.values():
                if value in precisionRange[0] or value in precisionRange[1] and not inPrecisionRange:
                    inPrecisionRange = True
            if not inPrecisionRange:
                errorRate += value
                invalidTickets.append(nearbyTicket)
    return errorRate, precisionRanges, yourTicket, [ticket for ticket in nearbyTickets if ticket not in invalidTickets]


def part2(precisionRange: dict, yourTicket: list, validTickets: list):
    allowed = {it:list() for it in range(len(validTickets[0]))}
    for it in range(len(validTickets[0])):
        zippedValuesOfEachTicket = list(zip(*validTickets))[it]
        for precision, interval in precisionRange.items():
            admitted = True
            for value in zippedValuesOfEachTicket:
                if value not in interval[0] and value not in interval[1] and admitted:
                    admitted = False
            if admitted:
                allowed[it].append(precision)
    
    while max(len(v) for v in allowed.values()) > 1:
        attributedItems = [(k,v[0]) for k,v in allowed.items() if len(v) == 1]
        for spot, attributedItem in attributedItems:
            for k,v  in allowed.items():
                if k != spot and attributedItem in v:
                    allowed[k].remove(attributedItem)
    
    allowed = {k:v[0] for k, v in allowed.items() if v[0].startswith('departure')}
    
    res = 1
    for k in allowed:
        res *= yourTicket[k]

    return res

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1[0]}")
    p2 = part2(*p1[1:])
    print(f"Part 2: {p2}")
    print(time()-a)

