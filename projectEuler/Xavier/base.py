import time
from collections import defaultdict
from functools import lru_cache
from math import sqrt

from utils import (add_one, is_prime, list_to_nbr, prime_numbers,
                   propagate_left_to_right)

if __name__ == '__main__' :
    start = time.time()

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
