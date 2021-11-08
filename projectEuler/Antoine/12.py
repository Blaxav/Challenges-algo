from time import time
import unittest
import math
a = time()


def get_divisors_amount(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 2
    return count

class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    it,triangle_number  = 1, 1
    while get_divisors_amount(triangle_number) < 499:
        it += 1
        triangle_number += it
    print(f"The answer is {triangle_number}")
    print(time()-a)

