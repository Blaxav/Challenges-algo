from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(character) for i in f.readline() for character in i.strip()]

def get_next_value(scheme: list, index: int, part: int):
    scheme_length = len(scheme)
    if part == 1:
        return scheme[index + 1] if index + 1 in range(scheme_length) else scheme[0]
    else:
        return scheme[index + scheme_length // 2] if index + scheme_length // 2 in range(scheme_length) else scheme[index + scheme_length // 2 - scheme_length]
            
def part1(scheme: list):
    captcha_sum = 0
    for index, elem in enumerate(scheme):
        if elem == get_next_value(scheme, index, 1):
            captcha_sum += elem
    return captcha_sum

def part2(scheme: list):
    captcha_sum = 0
    for index, elem in enumerate(scheme):
        if elem == get_next_value(scheme, index, 2):
            captcha_sum += elem
    return captcha_sum

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

