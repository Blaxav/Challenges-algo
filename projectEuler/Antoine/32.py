from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def is_pandigital_combination(x: int, y: int):
    return ''.join(sorted(str(x) + str(y) + str(x * y))) == "123456789"

# def second_range(x: int):
#     tenth_powers = 

if __name__ == "__main__":
    pandigital_product = list()
    for x in range(100, 10_000):
        for y in range(1, 100):
            if is_pandigital_combination(x, y) and x * y not in pandigital_product:
                pandigital_product.append(x * y)
    print(f"The answer is {sum(pandigital_product)}")
    print(time()-a)


