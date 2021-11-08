from time import time
import math
import unittest
a = time()


if __name__ == "__main__":
    # unittest.main()
    res = sum(int(it) for it in str(pow(2, 1000)))
    print(f"The answer is {res}")
    print(time()-a)

