from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i) for i in f.readline().strip().split(',')]

            
def part1(scheme: list, size: int):
    current_position, skip_size, current_list = 0, 0, list(range(size))
    for length in scheme:
        last_index_in_reversion = current_position + length
        if last_index_in_reversion <= len(current_list):
            current_list = current_list[:current_position] + current_list[current_position:last_index_in_reversion][::-1] + current_list[last_index_in_reversion:]
        else:
            reversed_list = (current_list[current_position:len(current_list)] + current_list[:last_index_in_reversion-len(current_list)])[::-1]
            current_list = reversed_list[len(current_list) - current_position:] + current_list[last_index_in_reversion-len(current_list):current_position] + reversed_list[:len(current_list)-current_position]
        current_position += length + skip_size
        while current_position not in range(len(current_list)):
            current_position -= len(current_list)
        skip_size += 1

    return current_list

def part2(scheme: list):
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1([3], 5), [2, 1, 0, 3, 4])
        self.assertEqual(part1([3, 4], 5), [4, 3, 0, 1, 2])
        self.assertEqual(part1([3, 4, 1, 5], 5), [3, 4, 2, 1, 0])
        self.assertEqual(part1([3, 4, 1, 5], 5), [3, 4, 2, 1, 0])


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 256)
    print(f"Part 1: {p1[0]*p1[1]}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

