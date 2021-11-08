from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def is_curious_fraction(numerator: int, denominator: int):
    str_numerator, str_denominator = str(numerator), str(denominator)
    if str_numerator == str_denominator[::-1] or (numerator % 10 == 0 and denominator % 10 == 0):
        return False
    elif str_numerator[0] in str_denominator:
        new_str_numerator, new_str_denominator = str_numerator[1], str_denominator.replace(str_numerator[0], '', 1)
        if int(new_str_numerator) / int(new_str_denominator) == numerator / denominator:
            return True
        else: 
            return False
    elif str_numerator[1] in str_denominator:
        new_str_numerator, new_str_denominator = str_numerator[0], str_denominator.replace(str_numerator[1], '', 1)
        if new_str_denominator != '0' and int(new_str_numerator) / int(new_str_denominator) == numerator / denominator:
            return True
        else: 
            return False
    else:
        return False

def gcd(x: int, y: int):
    while y:
        x, y = y, x % y
    
    return x

if __name__ == "__main__":
    total_numerator, total_denominator = 1, 1
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if is_curious_fraction(numerator, denominator):
                total_numerator *= numerator
                total_denominator *= denominator
    
    gcd = gcd(total_numerator, total_denominator)
    print(f"The answer is {total_denominator // gcd}")
    print(time()-a)

