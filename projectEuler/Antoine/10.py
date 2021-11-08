from time import time
import unittest
a = time()

def gen_primes():
    D = {}
    q = 2
    
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]       
        q += 1

class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    gen, res, prime = gen_primes(), 0, 0
    while prime < 2_000_000:
        res += prime
        prime = next(gen)
    print(f"The answer is {res}")
    print(time()-a)

