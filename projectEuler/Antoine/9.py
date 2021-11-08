from time import time
from math import sqrt
import unittest
a = time()
            
def findRes():
    for b in range(1, 1000):
        for c in range(b, 1000):
            if sqrt(pow(b, 2)+pow(c,2)).is_integer():
                d = int(sqrt(pow(b, 2)+pow(c,2)))
                if b + c + d == 1000:
                    return b*c*d

class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    print(f"The answer is {findRes()}")
    print(time()-a)

