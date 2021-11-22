from time import time
import unittest
a = time()

def readFilePart1():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i) for i in f.readline().strip().split(',')]

def readFilePart2():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(i) for i in f.readline().strip().split(',')]
            
def part1(scheme: list, current_list: list, current_position: int, skip_size: int):
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

    return current_list, current_position, skip_size

def ascii_list(scheme: str):
    return [ord(elem) for elem in scheme] + [17, 31, 73, 47, 23]

def part2(scheme: str):
    ascii_scheme = ascii_list(scheme)
    current_list, current_position, skip_size = list(range(256)), 0, 0
    for it in range(64):
        current_list, current_position, skip_size = part1(ascii_scheme, current_list, current_position, skip_size)
    xor_list, xor_result = list(), 0
    for count, elem in enumerate(current_list, 1):
        xor_result = xor_result ^ elem
        if count % 16 == 0:
            xor_list.append(xor_result)
            xor_result = 0
    hash_result = ""
    for elem in xor_list:
        hex_representation = hex(elem).split('x')[-1]
        hash_result += ("0" if len(hex_representation) == 1 else "") + hex_representation
    return hash_result

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1([3], 5, 0, 0)[0], [2, 1, 0, 3, 4])
        self.assertEqual(part1([3, 4], 5, 0, 0)[0], [4, 3, 0, 1, 2])
        self.assertEqual(part1([3, 4, 1, 5], 5, 0, 0)[0], [3, 4, 2, 1, 0])
        self.assertEqual(part1([3, 4, 1, 5], 5, 0, 0)[0], [3, 4, 2, 1, 0])


if __name__ == "__main__":
    # unittest.main()
    scheme = readFilePart1()
    p1 = part1(scheme, list(range(256)), 0, 0)
    print(f"Part 1: {p1[0][0]*p1[0][1]}")
    scheme = readFilePart2()
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)
