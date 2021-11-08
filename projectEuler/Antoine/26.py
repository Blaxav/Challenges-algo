from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

if __name__ == "__main__":
    max_recurring_cycle_size, max_denominator = 0, 0
    for num in range(1, 1001):
        divmod_results = []
        divmod_iteration = divmod(1, num)
        while divmod_iteration not in divmod_results:
            divmod_results.append(divmod_iteration)
            divmod_iteration = divmod(divmod_iteration[1] * 10, num)
        if len(divmod_results) - divmod_results.index(divmod_iteration) > max_recurring_cycle_size:
            max_recurring_cycle_size, max_denominator = len(divmod_results) - divmod_results.index(divmod_iteration), num

    print(f"The answer is {max_denominator}")
    print(time()-a)

