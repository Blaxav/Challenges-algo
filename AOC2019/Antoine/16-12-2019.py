from time import time
from itertools import chain, cycle
from collections import deque
a = time()

def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [int(i) for i in f.readline()]

def output(n: int, pattern: list):
    def repeatPattern(n: int, pattern: list):
        for item in cycle(pattern):
            for i in range(n):
                yield item
    iterator = repeatPattern(n, pattern)
    next(iterator)
    yield from iterator

def lastDigit(x: int):
    return abs(x) if -10 < x < 10 else int(str(x)[-1:])

def phase(inputList: list, pattern: list):
    new = []
    for a, b in enumerate(inputList, 1):
        new.append(abs(sum(x*y for x, y in zip(inputList, output(a, pattern))))%10)
    return new

def listToInt(inputList):
    return sum(10**(len(inputList)-a) * b for a, b in enumerate(inputList, 1))

def part1(inputList: list, pattern: list, steps: int):
    new = inputList
    for i in range(steps):
        new = phase(new, pattern)
    return listToInt(new[:8])

def part2(inputList: list, pattern: list, steps: int):
    offset = listToInt(inputList[:7])
    return res[offset:offset+7]

if __name__ == "__main__":
    vals = readFile()
    basePattern = [0, 1, 0, -1]
    p1 = part1(vals, basePattern, 100)
    print(f"Part 1: {p1}")
    # # p2 = part2(vals.book, stock, 'FUEL', 1, oreStock, p1)
    # # print(f"Part 2: {p2}")
    print(time()-a)

