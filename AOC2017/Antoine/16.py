from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip().split(',')

def spin(current_string: str, num: int):
    return current_string[-num:] + current_string[:len(current_string)-num]

def exchange(current_string: str, positions: int):
    return current_string[:positions[0]] + current_string[positions[1]] + current_string[positions[0] + 1:positions[1]] + current_string[positions[0]] + current_string[positions[1] + 1:]
            
def part1(current_string: str, scheme: list):
    for instruction in scheme:
        if instruction.startswith('s'):
            current_string = spin(current_string, int(instruction[1:]))
        elif instruction.startswith('x'):
            positions = sorted([int(b) for b in instruction.replace('x', '').split('/')])
            current_string = exchange(current_string, positions)
        elif instruction.startswith('p'):
            positions = sorted([current_string.find(b) for b in instruction.replace('p', '', 1).split('/')])
            current_string = exchange(current_string, positions)

    return current_string

def part2(current_string: str, scheme: list):
    states = []
    for it in range(1_000_000_000):
        if current_string in states:
            break
        else:
            states.append(current_string)

        for count, instruction in enumerate(scheme):
            if instruction.startswith('s'):
                current_string = spin(current_string, int(instruction[1:]))
            elif instruction.startswith('x'):
                positions = sorted([int(b) for b in instruction.replace('x', '').split('/')])
                current_string = exchange(current_string, positions)
            elif instruction.startswith('p'):
                positions = sorted([current_string.find(b) for b in instruction.replace('p', '', 1).split('/')])
                current_string = exchange(current_string, positions)

    return states[1_000_000_000 % it]

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1('abcdefghijklmnop', scheme)
    print(f"Part 1: {p1}")
    p2 = part2('abcdefghijklmnop', scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

