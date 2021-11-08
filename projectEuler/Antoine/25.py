from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(it) for it in i.strip().split()] for i in f.readlines()]

if __name__ == "__main__":
    # unittest.main()
    n_minus_two_value, n_minus_one_value, n_value, count = 1, 1, 0, 2
    while n_value < 10**999:
        count += 1
        n_value = n_minus_one_value + n_minus_two_value
        n_minus_two_value = n_minus_one_value
        n_minus_one_value = n_value


    print(f"The answer is {count}")
    print(time()-a)

