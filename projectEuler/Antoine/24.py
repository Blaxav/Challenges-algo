from time import time
from math import inf, sqrt
from collections import deque, defaultdict
from itertools import permutations
import unittest
a = time()


if __name__ == "__main__":
    for count, sorted_elem in enumerate(sorted(list(("".join(list(elem)) for elem in permutations("0123456789"))))):
        if count == 999_999:
            res = sorted_elem
    print(f"The answer is {res}")
    print(time()-a)

