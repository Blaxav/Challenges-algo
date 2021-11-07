import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers


def part1(path):
    k = 0
    fileIn = open(path)
    for line in fileIn:
        if k == 0:
            t0 = int(line.rstrip())
        else:
            bus = [int(i) for i in line.rstrip().split(',') if i != 'x']
        k += 1

    departures = []
    for t in bus:
        k = 1
        while k*t < t0:
            k += 1
        departures.append((t, k*t))

    departures.sort(key=lambda x: x[1])
    print(departures)
    print("Result: ",  (departures[0][1] - t0) * departures[0][0])
    fileIn.close()


if __name__ == '__main__':
    start = time.time()

    part1(sys.argv[1])

    # P2
    k = 0
    bus = []
    fileIn = open(sys.argv[1])
    for line in fileIn:
        if k == 1:
            k = 0
            for tstamp in line.rstrip().split(','):
                if tstamp != 'x':
                    bus.append((int(tstamp), k))
                k += 1
        k += 1

    bus.sort(key=lambda x: x[0], reverse=True)
    print(bus)

    freq = bus[0][0]
    offset = bus[0][1]

    for k in range(1, len(bus)):
        f2 = bus[k][0]
        ofs2 = bus[k][1]

        delta = offset - ofs2

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
