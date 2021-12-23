from time import time
import unittest
from math import sqrt
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [character for i in f.readlines() for character in i.replace(' \n', '') ]

def get_first_position(scheme: list):
    it = 0
    while scheme[it] != '|':
        it += 1
    
    return it

def get_neighbours(position: int, scheme: list):
    scheme_width = int(sqrt(len(scheme)))
    if position % scheme_width == 0:
        return [scheme[position + delta] if position + delta in range(len(scheme)) else ' ' for delta in (-scheme_width, -position, 1, scheme_width)]
    elif (position + 1) % scheme_width == 0:
        return [scheme[position + delta] if position + delta in range(len(scheme)) else ' ' for delta in (-scheme_width, -1, -position, scheme_width)]
    else:
        return [scheme[position + delta] if position + delta in range(len(scheme)) else ' ' for delta in (-scheme_width, -1, 1, scheme_width)]

def get_next_direction(position: int, scheme: list, direction: str):
    neighbours = get_neighbours(position, scheme)
    if direction in ('up', 'down'):
        if neighbours[1] != ' ':
            return 'left'
        else:
            return 'right'
    else:
        if neighbours[0] != ' ':
            return 'up'
        else:
            return 'down'

def part1(scheme: list):
    first_position = get_first_position(scheme)
    current_elem = scheme[first_position]
    current_position = first_position
    scheme_width = int(sqrt(len(scheme)))
    direction_offset = {'up': -scheme_width, 'left': -1, 'right': 1, 'down': scheme_width}
    current_direction = 'down'
    string = ''
    count = -1
    while current_elem != ' ':
        current_elem = scheme[current_position]
        if current_elem.isupper():
            string += current_elem
        elif current_elem == '+':
            current_direction = get_next_direction(current_position, scheme, current_direction)
        current_position += direction_offset[current_direction]
        count += 1
    return string, count

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1[0]}")
    print(f"Part 2: {p1[1]}")
    print(time()-a)

