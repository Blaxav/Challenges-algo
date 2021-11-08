from time import time
from math import inf, sqrt
from collections import deque, defaultdict
import unittest
a = time()

def next_cell(current_cell: tuple, interval_number: int):
    if current_cell[0] == -interval_number and -interval_number <= current_cell[1] < interval_number:
        return (current_cell[0], current_cell[1] + 1), interval_number
    elif current_cell[1] == -interval_number and -interval_number < current_cell[0] <= interval_number:
        return (current_cell[0] - 1, current_cell[1]), interval_number
    elif current_cell[0] == interval_number and -interval_number < current_cell[1] < interval_number:
        return (current_cell[0], current_cell[1] - 1), interval_number
    elif current_cell[1] == interval_number and -interval_number <= current_cell[0] <= interval_number:
        if current_cell[0] == interval_number:
            return (current_cell[0] + 1, current_cell[1]), interval_number + 1
        else:
            return (current_cell[0] + 1, current_cell[1]), interval_number

if __name__ == "__main__":
    current_cell, current_value, interval_number, diagonal_sum = (0, 0), 1, 0, 0
    while interval_number <= 500:
        if abs(current_cell[0]) == abs(current_cell[1]):
            diagonal_sum += current_value
        current_cell, interval_number = next_cell(current_cell, interval_number)
        current_value += 1
    print(f"The answer is {diagonal_sum}")
    print(time()-a)

