from time import time
from math import inf, sqrt
from collections import deque, defaultdict
from itertools import product
import unittest
a = time()


if __name__ == "__main__":
    combinations = list()
    for int_a, int_b in product(range(2, 101), range(2, 101)):
        combinations.append(int_a ** int_b)
    print(f"The answer is {len(set(combinations))}")
    print(time()-a)

