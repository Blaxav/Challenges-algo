from time import time
from copy import deepcopy
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[char for char in i.strip()] for i in f.readlines()]

def getAdjacentSeats(scheme:list, x: int, y: int):
    return [(x+xOffset,y+yOffset) for xOffset in [-1, 0, 1] for yOffset in [-1, 0, 1] if x+xOffset in range(len(scheme[0])) and y+yOffset in range(len(scheme)) and (xOffset or yOffset)]


def getVisibleSeats(scheme:list, x: int, y: int):
    visibleSeats = list()
    for xOffset in [-1, 0, 1]:
        for yOffset in [-1, 0, 1]:
            if not xOffset and not yOffset:
                continue
            xVisibleSeat, yVisibleSeat = x + xOffset, y + yOffset
            while xVisibleSeat in range(len(scheme[y])) and yVisibleSeat in range(len(scheme)) and scheme[yVisibleSeat][xVisibleSeat] != 'L':
                xVisibleSeat += xOffset
                yVisibleSeat += yOffset
            if xVisibleSeat in range(len(scheme[y])) and yVisibleSeat in range(len(scheme)) and scheme[yVisibleSeat][xVisibleSeat] == 'L':
                visibleSeats.append((xVisibleSeat, yVisibleSeat))

    return visibleSeats

def generateSeatsDict(scheme:list, part: int):
    seatsDict = dict()
    for y in range(len(scheme)):
        for x in range(len(scheme[y])):
            if scheme[y][x] == 'L':
                if part == 1:
                    seatsDict[(x, y)] = getAdjacentSeats(scheme, x, y)
                if part == 2:
                    seatsDict[(x, y)] = getVisibleSeats(scheme, x, y)
    
    return seatsDict

def transformScheme(scheme: list, seatsDict: dict, tolerence: int):
    newScheme = deepcopy(scheme)
    changesAmount = 0
    for y in range(len(scheme)):
        for x in range(len(scheme[y])):
            if scheme[y][x] != '.':
                seats = [scheme[elem[1]][elem[0]] for elem in seatsDict[(x, y)]]
                if scheme[y][x] == 'L' and '#' not in seats:
                    newScheme[y][x] = '#'
                    changesAmount += 1
                elif scheme[y][x] == '#' and seats.count('#') >= tolerence:
                    newScheme[y][x] = 'L'
                    changesAmount += 1

    return newScheme, changesAmount

def part1(scheme: list):
    newScheme, changesAmount, seatsDict = deepcopy(scheme), 1, generateSeatsDict(scheme, 1)
    while changesAmount > 0:
        newScheme, changesAmount = transformScheme(newScheme, seatsDict, 4)
    return sum(elem.count('#') for elem in newScheme)

def part2(scheme: list):
    newScheme, changesAmount, seatsDict = deepcopy(scheme), 1, generateSeatsDict(scheme, 2)
    while changesAmount > 0:
        newScheme, changesAmount = transformScheme(newScheme, seatsDict, 5)
    return sum(elem.count('#') for elem in newScheme)

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

