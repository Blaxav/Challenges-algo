from time import time
import math
import unittest
from itertools import permutations
a = time()



if __name__ == "__main__":
    # unittest.main()
    n = 20
    paths_amount = int(math.factorial(2*n)/(pow(math.factorial(n),2)))
    print(f"The answer is {paths_amount}")
    print(time()-a)

