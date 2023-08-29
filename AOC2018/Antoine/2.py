from time import time
import unittest
from collections import Counter
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def count_letters_occurences(string: str):
    return Counter(string)
            
def part1(scheme: list):
    two_occurences_amount, three_occurences_amount = 0, 0
    for string in scheme:
        if 2 in count_letters_occurences(string).values():
            two_occurences_amount += 1
        if 3 in count_letters_occurences(string).values():
            three_occurences_amount += 1

    return two_occurences_amount * three_occurences_amount

def extract_sub_string(string: str, index: int):
    return string[:index] + string[index+1:]

def part2(scheme: list):
    for first_string in scheme:
        for it in range(len(first_string)):
            for second_string in scheme:
                if first_string != second_string:
                    if extract_sub_string(first_string, it) == extract_sub_string(second_string, it):
                        return extract_sub_string(first_string, it)

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

