from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        coordinates, instructions = list(), list()
        for i in f.readlines():
            if ',' in i:
                coordinates.append(tuple(int(elem) for elem in i.strip().split(',')))
            elif '=' in i:
                instruction = i.strip().split('=')
                instructions.append([instruction[0][-1], int(instruction[1])])

        return coordinates, instructions

            
def part1(coordinates: list, instructions: list, limit: int):
    positions_dict = {k:v for k, v in enumerate(coordinates)}
    for instruction in instructions[:limit]:
        for k, v in positions_dict.items():
            if instruction[0] == 'x' and v[0] > instruction[1]:
                positions_dict[k] = (instruction[1] * 2 - v[0], v[1])
            if instruction[0] == 'y' and v[1] > instruction[1]:
                positions_dict[k] = (v[0], instruction[1] * 2 - v[1])

    return positions_dict

def part2(coordinates: list, instructions: list):
    final_positions_list = list(set(part1(coordinates, instructions, len(instructions)).values()))
    max_x, max_y = max(elem[0] for elem in final_positions_list), max(elem[1] for elem in final_positions_list)
    for y in range(max_y + 1):
        current_sentence = ''
        for x in range(max_x + 1):
            if (x, y) in final_positions_list:
                current_sentence += '#'
            else:
                current_sentence += ' '
        print(current_sentence)

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    coordinates, instructions = readFile()
    print(max(coordinates, key=lambda x:x[0]))
    p1 = part1(coordinates, instructions, 1)
    print(f"Part 1: {len(set(p1.values()))}")
    print(f"Part 2:")
    part2(coordinates, instructions)
    print(time()-a)

