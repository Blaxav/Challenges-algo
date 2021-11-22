from time import time
import unittest
import knothashes
from collections import deque
from math import sqrt
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def hex_to_binary(hex_number: str):
    return str(bin(int(hex_number, 16)))[2:].zfill(128)
            
def part1(scheme: str):
    return "".join([hex_to_binary(knothashes.part2(scheme + "-" + str(it))) for it in range(128)])

def get_neighbours(position: int, scheme: str):
    scheme_length = int(sqrt(len(scheme)))
    if position % scheme_length == 0:
        left_right_moves = [1]
    elif (position + 1) % scheme_length == 0:
        left_right_moves = [-1]
    else:
        left_right_moves = [-1, 1]
    moves = [scheme_length, -scheme_length] + left_right_moves

    return sorted([position + move for move in moves if position + move in range(len(scheme)) and scheme[position + move] == '1'])

def explore_group(position: int, scheme: str):
    positions_to_explore, group = deque([position]), []
    scheme[position] = '0'
    while positions_to_explore:
        current_position = positions_to_explore.pop()
        for new_position in get_neighbours(current_position, scheme):
            positions_to_explore.append(new_position)
            scheme[new_position] = '0' 
        group.append(current_position)
    return scheme

def part2(scheme: str):
    scheme = [elem for elem in scheme]
    group_amount, grouped_positions = 0, list()
    for position, elem in enumerate(scheme):
        if elem == '1':
            scheme = explore_group(position, scheme)
            group_amount += 1

    return group_amount

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1('flqrgnkx').count('1'), 8108)
        self.assertEqual(part2(part1('flqrgnkx')), 1242)

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1.count('1')}")
    p2 = part2(p1)
    print(f"Part 2: {p2}")
    print(time()-a)

