from time import time
from collections import defaultdict
import unittest
from copy import deepcopy
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(num) for num in i.strip().replace('#', '').replace(' @ ', ' ').replace(',', ' ').replace(':', '').replace('x', ' ').split(' ')] for i in f.readlines()]

def get_top_left_position(square: list):
    return square[1] + 1000 * square[2]

def get_square_positions(square: list):
    square_positions = list()
    for height in range(square[4]):
        first_line_position = get_top_left_position(square) + height * 1000
        for width in range(square[3]):
            current_position = first_line_position + width
            square_positions.append(current_position)

    return square_positions

def get_dict_positions(scheme: list):
    positions = defaultdict(int)
    for square in scheme:
        for square_position in get_square_positions(square):
            positions[square_position] += 1
    
    return positions

def get_overlapped_positions(dict_positions: dict):
    return [k for k, v in dict_positions.items() if v > 1]
            
def part1(scheme: list):
    dict_positions = get_dict_positions(scheme)

    return len(get_overlapped_positions(dict_positions))

def part2(scheme: list):
    dict_positions = get_dict_positions(scheme)
    for square in scheme:
        if all(dict_positions[elem] == 1 for elem in get_square_positions(square)):
            return square[0]

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(get_top_left_position([1, 1, 3, 4, 4]), 3001)
        self.assertEqual(get_top_left_position([2, 3, 1, 4, 4]), 1003)
        self.assertEqual(get_top_left_position([3, 5, 5, 2, 2]), 5005)
        self.assertEqual(get_square_positions([1, 1, 3, 4, 4]), [3001, 3002, 3003, 3004, 4001, 4002, 4003, 4004, 5001, 5002, 5003, 5004, 6001, 6002, 6003, 6004])
        self.assertEqual(get_square_positions([2, 3, 1, 4, 4]), [1003, 1004, 1005, 1006, 2003, 2004, 2005, 2006, 3003, 3004, 3005, 3006, 4003, 4004, 4005, 4006])
        self.assertEqual(get_square_positions([3, 5, 5, 2, 2]), [5005, 5006, 6005, 6006])
        self.assertEqual(part1([[1, 1, 3, 4, 4], [2, 3, 1, 4, 4], [3, 5, 5, 2, 2]]), 4)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

