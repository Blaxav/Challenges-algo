from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return int(f.readline().strip())

            
def part1(scheme: int):
    spinlock, current_position = [0], 0
    for it in range(1, 2018):
        inserting_position = (current_position + scheme) % len(spinlock) + 1
        spinlock = spinlock[:inserting_position] + [it] + spinlock[inserting_position:]
        current_position = inserting_position

    return spinlock[current_position + 1]

def part2(scheme: int):
    current_position, value_after_zero = 0, 0
    for it in range(1, 50_000_001):
        current_position = (current_position + scheme) % it + 1
        if current_position == 1:
            value_after_zero = it
    return value_after_zero

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

