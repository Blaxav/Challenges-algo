from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def sum_of_fifth_power_digit(n: int):
    return sum(int(digit) ** 5 for digit in str(n))

if __name__ == "__main__":
    res = 0
    for it in range(10, 1_000_000):
        if it == sum_of_fifth_power_digit(it):
            res += it
    print(f"The answer is {res}")
    print(time()-a)

