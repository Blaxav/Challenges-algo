from time import time
import unittest
a = time()
            
class Tests(unittest.TestCase):

    def test(self):
        pass

def isDivisble(num: int):
    for elem in [7,8,9,11,13,16,17,18,19]:
        if num % elem:
            return False
    return True

if __name__ == "__main__":
    # unittest.main()
    res = 2520
    while not isDivisble(res):
        res += 60
    print(f"The answer is {res}")
    print(time()-a)

