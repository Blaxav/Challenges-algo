from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def findRow(instruction: str):
    rowInstruction = instruction[:7]
    rowList = list(range(128))
    for char in rowInstruction:
        rowList = rowList[:int(len(rowList)/2)] if char =='F' else rowList[-int(len(rowList)/2):]

    return rowList[0]

def findSeat(instruction: str):
    seatInstruction = instruction[-3:]
    seatList = list(range(8))
    for char in seatInstruction:
        seatList = seatList[:int(len(seatList)/2)] if char =='L' else seatList[-int(len(seatList)/2):]

    return seatList[0]

            
def part1(scheme: list):
    return max([findRow(elem) * 8 + findSeat(elem) for elem in scheme])

def part2(scheme: list):
    idList = [findRow(elem) * 8 + findSeat(elem) for elem in scheme]
    for num in range(min(idList), max(idList)):
        if num not in idList:
            return num

            
class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

