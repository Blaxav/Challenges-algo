from time import time
from math import inf, sqrt
from collections import deque, defaultdict
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

def gen_divisors(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n and i != 1:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor

def get_divisors_amount(num):
    count = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            count += 2
    return count

def is_abundant_number(num):
    return True if sum(gen_divisors(num)) > num else False


class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    res = 0
    abundant_numbers = [it for it in range(12, 28124) if is_abundant_number(it)]
    written_as_sum_of_abundant_numbers = []
    for first_number in abundant_numbers:
        for second_number in abundant_numbers:
            if first_number + second_number <= 28123:
                written_as_sum_of_abundant_numbers.append(first_number+second_number)
    written_as_sum_of_abundant_numbers = list(set(written_as_sum_of_abundant_numbers))
    for number in range(28124):
        if number not in written_as_sum_of_abundant_numbers:
            res += number
    print(f"The answer is {res}")
    print(time()-a)

