from time import time
import unittest
a = time()

def fibonacci(n: int):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fibonacci(n-1)+fibonacci(n-2)
            
class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    res, sequence, ind = 2, {0: 1, 1: 2}, 2
    while sequence[ind-1]+sequence[ind-2] < 4_000_000:
        sequence[ind] = sequence[ind-1]+sequence[ind-2]
        if sequence[ind] % 2 == 0:
            res += sequence[ind]
        ind += 1
    print(f"The answer is {res}")
    print(time()-a)

