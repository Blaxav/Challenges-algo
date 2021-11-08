from time import time
from collections import defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return int(f.readline().strip())

def next_cell(current_cell: tuple, interval_number: int):
    if current_cell[0] == interval_number and -interval_number < current_cell[1] < interval_number:
        return (current_cell[0], current_cell[1] + 1), interval_number
    elif current_cell[1] == interval_number and -interval_number < current_cell[0] <= interval_number:
        return (current_cell[0] - 1, current_cell[1]), interval_number
    elif current_cell[0] == -interval_number and -interval_number < current_cell[1] <= interval_number:
        return (current_cell[0], current_cell[1] - 1), interval_number
    elif current_cell[1] == -interval_number and -interval_number <= current_cell[0] <= interval_number:
        if current_cell[0] == interval_number:
            return (current_cell[0] + 1, current_cell[1]), interval_number + 1
        else:
            return (current_cell[0] + 1, current_cell[1]), interval_number


def part1(scheme: int):
    current_cell, interval_number = (0, 0), 0
    for it in range(scheme - 1):
        current_cell, interval_number = next_cell(current_cell, interval_number)
    return abs(current_cell[0]) + abs(current_cell[1])



def part2(scheme: list):
    grid, current_cell, interval_number, current_value = defaultdict(int), (0, 0), 0, 1
    grid[current_cell] = current_value
    while current_value < scheme:
        current_cell, interval_number = next_cell(current_cell, interval_number)
        current_value = sum(grid[(current_cell[0] + x, current_cell[1] + y)] for x in range(-1, 2) for y in range(-1, 2) if abs(x) + abs(y) > 0)
        grid[current_cell] = current_value
    return current_value

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

