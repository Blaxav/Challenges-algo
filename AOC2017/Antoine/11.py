from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip().split(',')


def part1(scheme: list):
    x, y, further_position = 0, 0, 0
    for elem in scheme: 
        if elem == 'n':
            y += 1
        elif elem == 's':
            y -= 1
        elif elem == 'ne':
            x += 0.5
            y += 0.5
        elif elem == 'nw':
            x -= 0.5
            y += 0.5
        elif elem == 'se':
            x += 0.5
            y -= 0.5
        elif elem == 'sw':
            x -= 0.5
            y -= 0.5
        if abs(x) + abs(y) > further_position:
            further_position = abs(x) + abs(y)

    return abs(x) + abs(y), further_position


class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1(["ne","ne","ne"]), 3)
        self.assertEqual(part1(["ne","ne","sw","sw"]), 0)
        self.assertEqual(part1(["ne","ne","s","s"]), 2)
        self.assertEqual(part1(["se","sw","se","sw","sw"]), 3)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {int(p1[0])}")
    print(f"Part 2: {int(p1[1])}")
    print(time()-a)

