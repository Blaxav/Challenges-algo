from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def is_prime(n: int):
    if n in [2, 3]: 
        return True
    if n % 2 == 0 or n < 2: 
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False    
    return True


def polynom(n: int, coefficient_a: int, coefficient_b: int):
    return n**2 + coefficient_a * n + coefficient_b


if __name__ == "__main__":
    max_prime_amount, max_product = 40, 41
    for coefficient_a in range(-999, 1000):
        for coefficient_b in range(-1000, 1001):
            n_iterator = 0
            while is_prime(polynom(n_iterator, coefficient_a, coefficient_b)):
                n_iterator += 1
            if n_iterator > max_prime_amount:
                max_prime_amount, max_product = n_iterator, coefficient_a * coefficient_b 
    print(f"The answer is {max_product}")
    print(time()-a)

