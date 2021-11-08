from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
from math import factorial
a = time()

def is_curious_number(x: int):
    return x == sum(factorial(int(elem)) for elem in str(x))

if __name__ == "__main__":
    number, res = 10, 0
    while number < 100_000:
        if is_curious_number(number):
            res += number
        number += 1
    print(f"The answer is {res}")
    print(time()-a)

