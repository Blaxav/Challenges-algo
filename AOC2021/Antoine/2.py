from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

            
def part1(scheme: list):
    horizontal_position, depth = 0, 0
    for elem in scheme:
        instruction = elem.split(' ')
        if instruction[0] == 'forward':
            horizontal_position += int(instruction[1])
        elif instruction[0] == 'down':
            depth += int(instruction[1])
        elif instruction[0] == 'up':
            depth -= int(instruction[1])

    return horizontal_position * depth

def part2(scheme: list):
    horizontal_position, depth, aim = 0, 0, 0
    for elem in scheme:
        instruction = elem.split(' ')
        if instruction[0] == 'forward':
            horizontal_position += int(instruction[1])
            depth += int(instruction[1]) * aim
        elif instruction[0] == 'down':
            aim += int(instruction[1])
        elif instruction[0] == 'up':
            aim -= int(instruction[1])
    
    return horizontal_position * depth

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

