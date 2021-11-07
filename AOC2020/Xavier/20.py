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

    def fillEdges(self, edges):


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
            curTile.fillEdges(edges)
            tiles.append(curTile)
        elif line.split()[0] == "Tile":
            curTile = Tile()
            curTile.id = line.split()[1][:-1]
            lineId = 0
            # N E S W
            edges = ["", "", "", ""]
        else:
            print(line)
            if lineId == 0:
                size = len(line.rstrip())

                edges[0] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()])
                edges[3] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()[0]])
                edges[1] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()[-1]])
            elif lineId < size - 1:
                edges[3] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()[0]])
                edges[1] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()[-1]])
            else:
                edges[3] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()[0]])
                edges[1] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()[-1]])
                edges[2] += "".join(["0" if x ==
                                     "." else "1" for x in line.rstrip()])
            lineId += 1

    print(edges)
    print([int(edge, 2) for edge in edges])

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
