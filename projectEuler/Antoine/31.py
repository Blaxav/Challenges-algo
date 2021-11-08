from time import time
from math import inf, sqrt
from collections import deque, defaultdict
from itertools import product
import unittest
a = time()


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100]
    possibilities = {k: range(200 // k + 1) for k in coins}
    res = 0
    for int_200 in range(2):
        if int_200 * 200 == 200:
            res += 1
        elif int_200 * 200 > 200:
            break
        else:
            for int_100 in range(3):
                if int_200 * 200 + int_100 * 100 == 200:
                    res += 1
                elif int_200 * 200 + int_100 * 100 > 200:
                    break
                else:
                    for int_50 in range(5):
                        if int_200 * 200 + int_100 * 100 + int_50 * 50 == 200:
                            res += 1
                        elif int_200 * 200 + int_100 * 100 + int_50 * 50 > 200:
                            break
                        else:
                            for int_20 in range(11):
                                if int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 == 200:
                                    res += 1
                                elif int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 > 200:
                                    break
                                else: 
                                    for int_10 in range(21):
                                        if int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 == 200:
                                            res += 1
                                        elif int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 > 200:
                                            break
                                        else: 
                                            for int_5 in range(41):
                                                if int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 + int_5 * 5 == 200:
                                                    res += 1
                                                elif int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 + int_5 * 5 > 200:
                                                    break
                                                else:
                                                    for int_2 in range(101):
                                                        if int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 + int_5 * 5 + int_2 * 2 == 200:
                                                            res += 1
                                                        elif int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 + int_5 * 5 + int_2 * 2 > 200:
                                                            break
                                                        else:
                                                            for int_1 in range(201):
                                                                if int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 + int_5 * 5 + int_2 * 2 + int_1 * 1 == 200:
                                                                    res += 1
                                                                elif int_200 * 200 + int_100 * 100 + int_50 * 50 + int_20 * 20 + int_10 * 10 + int_5 * 5 + int_2 * 2 + int_1 * 1 > 200:
                                                                    break
                                                                else:
                                                                    continue
                                    
    print(f"The answer is {res}")
    print(time()-a)
