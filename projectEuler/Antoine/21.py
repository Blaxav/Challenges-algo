from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(it) for it in i.strip().split()] for i in f.readlines()]


def gen_divisors(n):
    large_divisors = []
    for i in range(1, n):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(int(n / i))



class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    passed, amicables_sum = [], 0
    for elem in range(10001):
        if elem not in passed:
            divisors_sum = sum(gen_divisors(elem))
            if sum(gen_divisors(divisors_sum)) == elem and elem != divisors_sum:
                amicables_sum += elem + divisors_sum
            passed.append(elem)
            passed.append(divisors_sum)
    print(f"The answer is {amicables_sum}")
    print(time()-a)

