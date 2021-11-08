from time import time
import math
import unittest
a = time()


def sequence(num: int):
    return num / 2 if num % 2 == 0 else 3 * num + 1

def chain_length(num: int):
    length = 1
    while num != 1:
        num = sequence(num)
        length += 1

    return length


class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    max_length, starting_number = 1, 1
    for it in range(1, 1000000):
        it_length = chain_length(it)
        if it_length > max_length:
            max_length, starting_number = it_length, it
    print(f"The answer is {starting_number}")
    print(time()-a)

