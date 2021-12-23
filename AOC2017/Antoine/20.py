from time import time
import unittest
from collections import defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        coordinates = defaultdict(dict)
        for count, line in enumerate(f.readlines()):
            split_line = line.split(', ')
            for coordinate in split_line:
                coordinate = coordinate.replace('=<', '').replace('>', '')
                coordinates[count][coordinate[0]] = {axis:int(it) for axis, it in zip(('x', 'y', 'z'), coordinate[1:].split(','))}

        return coordinates

            
def part1(scheme: dict):
    return min(scheme.items(), key=lambda x: sum(abs(it) for it in x[1]['a'].values()))[0]

def update_speed_and_positions(scheme: dict):
    for key in scheme:
        for axis in ('x', 'y', 'z'):
            scheme[key]['v'][axis] += scheme[key]['a'][axis]
            scheme[key]['p'][axis] += scheme[key]['v'][axis]
    
    return scheme

def delete_particules(scheme: dict):
    position_list = [coordinates['p'] for coordinates in scheme.values()]
    positions_with_several_particules = [position for position in position_list if position_list.count(position) > 1]

    indexes_to_delete = list()
    for key in scheme:
        if scheme[key]['p'] in positions_with_several_particules:
            indexes_to_delete.append(key)
    for index_to_delete in indexes_to_delete:
        del scheme[index_to_delete]

    return scheme

def part2(scheme: dict):
    for it in range(100):
        scheme = update_speed_and_positions(scheme)
        scheme = delete_particules(scheme)

    return len(scheme)

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

