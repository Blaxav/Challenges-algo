from time import time
import unittest
a = time()
            
class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    res = 0
    for number in range(1000):
        if number % 3 == 0 or number % 5 == 0:
            res += number
    print(f"The answer is {res}")
    print(time()-a)

