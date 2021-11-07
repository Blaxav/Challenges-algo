import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime


if __name__ == '__main__' :
    start = time.time()

    for z in range(1, 10000):
        if str(z)[0] == '9':
            res = str(z)
            i = 1
            while len(res) < 9:
                i += 1
                res += str(i*z)
            if len(res) == 9 and sorted(res) == [ str(i) for i in range(1, 10)]:
                print("coucou ", z, res) 
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))