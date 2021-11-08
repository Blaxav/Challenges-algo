from time import time
import unittest
a = time()
            
class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    res = abs(sum(pow(a,2) for a in range(101)) - pow(sum(a for a in range(101)),2))
    print(f"The answer is {res}")
    print(time()-a)

