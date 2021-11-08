from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def part1(scheme: list):
    keypad = [['1','2','3'], ['4','5','6'], ['7','8','9']]
    row, col = 1, 1
    code = ''
    for line in scheme:
        for instruction in line:
            if instruction == 'U':
                row = max(0, row-1)
            if instruction == 'D':
                row = min(2, row+1)
            if instruction == 'L':
                col = max(0, col-1)
            if instruction == 'R':
                col = min(2, col+1)
        code = code + keypad[row][col]
    return code

def part2(scheme: list):
    keypad = [['', '', '1', '', ''], ['','2','3','4',''], ['5','6','7','8','9'], ['','A','B','C',''], ['','','D','','']]
    row, col = 2, 0
    code = ''
    for line in scheme:
        for instruction in line:
            if instruction == 'U':
                row = max(0, row-1)
                if keypad[row][col] == '':
                    row += 1
            if instruction == 'D':
                row = min(4, row+1)
                if keypad[row][col] == '':
                    row -= 1
            if instruction == 'L':
                col = max(0, col-1)
                if keypad[row][col] == '':
                    col += 1
            if instruction == 'R':
                col = min(4, col+1)
                if keypad[row][col] == '':
                    col -= 1
        code = code + keypad[row][col]
    return code

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

