from time import time
import unittest
a = time()
            
class Tests(unittest.TestCase):

    def test(self):
        pass

def isPalindrom(number:str):
    return number == number[::-1]

if __name__ == "__main__":
    # unittest.main()
    res = 0
    for firstn in range(100, 1000):
        for secondn in range(firstn, 1000):
            if isPalindrom(str(firstn*secondn)) and firstn*secondn > res:
                res = firstn*secondn
    print(f"The answer is {res}")
    print(time()-a)

