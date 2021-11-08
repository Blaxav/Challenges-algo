from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [name.replace('"', '') for name in f.readline().strip().split('","')]

def char_to_position(letter: str):
    return ord(letter) - 64

class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    names = readFile()
    names.sort()
    res = sum(sum(char_to_position(letter) for letter in name) * pos for pos, name in enumerate(names, 1))
    print(f"The answer is {res}")
    print(time()-a)

