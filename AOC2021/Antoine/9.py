from time import time
import unittest
from math import sqrt
from collections import deque
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(elem) for i in f.readlines() for elem in i.strip()]

def get_neighbours(position: int, scheme: list):
    scheme_width = int(sqrt(len(scheme)))
    if position % scheme_width == 0:
        return (position + delta for delta in [-scheme_width, 1, scheme_width] if position + delta in range(len(scheme)))
    elif (position + 1) % scheme_width == 0:
        return (position + delta for delta in [-scheme_width, -1, scheme_width] if position + delta in range(len(scheme)))
    else:
        return (position + delta for delta in [-scheme_width, -1, 1, scheme_width] if position + delta in range(len(scheme)))

def is_low_point(position: int, scheme: list):
    if all(scheme[neighbour] > scheme[position] for neighbour in get_neighbours(position, scheme)):
        return True
    else:
        return False

def get_risk_level(position: int, scheme: list):
    if is_low_point(position, scheme):
        return scheme[position] + 1
    else:
        return 0
            
def part1(scheme: list):
    return sum(get_risk_level(position, scheme) for position in range(len(scheme)))

def get_basin_size(position: int, scheme: list):
    basin_positions_to_explore, basin = deque([position]), [position]
    while basin_positions_to_explore:
        current_position = basin_positions_to_explore.pop()
        for neighbour in get_neighbours(current_position, scheme):
            if neighbour not in basin_positions_to_explore and neighbour not in basin and scheme[position] < scheme[neighbour] < 9:
                basin_positions_to_explore.append(neighbour)
                basin.append(neighbour)
    
    return len(basin)

def part2(scheme: list):
    basins = list()
    for position in range(len(scheme)):
        if is_low_point(position, scheme):
            basins.append(get_basin_size(position, scheme))

    basins = sorted(basins, reverse=True)[:3]

    return basins[0] * basins[1] * basins[2]

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

