from time import time
import unittest
from collections import deque
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def rect(screen: list, rowRange: int, colRange: int):
    for row in range(rowRange):
        for col in range(colRange):
            screen[row][col] = 1
    return screen

def rotateRow(screen: list, row: int, shift: int):
    screen[row].rotate(shift)
    return screen

def rotateCol(screen: list, col: int, shift: int):
    newCol = deque([screen[it][col] for it in range(len(screen))])
    newCol.rotate(shift)
    for it in range(len(screen)):
        screen[it][col] = newCol[it]
    return screen

def part1(scheme: list):
    screen = [deque([0]*50) for it in range(6)]
    for elem in scheme:
        if elem.startswith('rect'):
            info = elem[5:].split('x')
            screen = rect(screen, int(info[1]), int(info[0]))
        elif elem.startswith('rotate row'):
            info = elem[13:].split(' by ')
            screen = rotateRow(screen, int(info[0]), int(info[1]))
        elif elem.startswith('rotate column'):
            info = elem[16:].split(' by ')
            screen = rotateCol(screen, int(info[0]), int(info[1]))    
    return screen

def part2(scheme: list):
    screen = part1(scheme)
    for elem in screen:
        line = ''
        for num in elem:
            if num == 1:
                line += 'x'
            else:
                line += ' '
        print(line)
    return 'AFBUPZBJPS'


class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {sum([sum(elem) for elem in p1])}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

