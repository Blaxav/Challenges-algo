from time import time
from math import inf, factorial, sqrt
from collections import deque, defaultdict
import unittest
a = time()



if __name__ == "__main__":
    # unittest.main()
    res = sum(int(elem) for elem in str(factorial(100)))
    print(f"The answer is {res}")
    print(time()-a)

