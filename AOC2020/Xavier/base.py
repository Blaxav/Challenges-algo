import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers


class Tile:
    def __init__(self):
        self.north = [0, 0]
        self.south = [0, 0]
        self.east = [0, 0]
        self.west = [0, 0]
        self.id = 0
        self.state = [0, 0, 0, 0]
        self.flip = [0, 0]
        self.rotate = 0


if __name__ == '__main__':
    start = time.time()

    tiles = []
    lineId = 0
    curTile = Tile()

    lines = []
    size = 0
    fileIn = open(sys.argv[1])
    for line in fileIn:
        if line == "\n":
            if line.split()[0] == "Tile":
                curTile = Tile()
                curTile.id = line.split()[1][:-1]
                lineId = 0
                # N E S W
                lines = ["", "", "", ""]
        else:
            if lineId == 0:
                size = len(line.rstrip())
                lines[0] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()])
                lines[3] += "".join(["0" if x ==
                                     "." else "1" for x in line[0].rstrip()])
                lines[1] += "".join(["0" if x ==
                                     "." else "1" for x in line[-1].rstrip()])
            elif lineId < size - 1:
                lines[3] += "".join(["0" if x ==
                                     "." else "1" for x in line[0].rstrip()])
                lines[1] += "".join(["0" if x ==
                                     "." else "1" for x in line[-1].rstrip()])
            else:
                lines[3] += "".join(["0" if x ==
                                     "." else "1" for x in line[0].rstrip()])
                lines[1] += "".join(["0" if x ==
                                     "." else "1" for x in line[-1].rstrip()])
                lines[2] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()])
            lienId += 1
    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
