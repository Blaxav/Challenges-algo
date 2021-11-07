import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers


class Boat:
    def __init__(self):
        self.pos = [0, 0]
        self.dir = [0, 1]

    def apply(self, command):
        vect = {
            'N': [1, 0],
            'S': [-1, 0],
            'E': [0, 1],
            'W': [0, -1],
            'F': self.dir
        }

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if command[0] == 'R':
            numsRotation = int(int(command[1:])/90)
            for rot in range(numsRotation):
                index = (dirs.index(self.dir) - 1) % 4
                for k in range(2):
                    self.dir[k] = dirs[index][k]
        elif command[0] == 'L':
            numsRotation = int(int(command[1:])/90)
            for rot in range(numsRotation):
                index = (dirs.index(self.dir) + 1) % 4
                for k in range(2):
                    self.dir[k] = dirs[index][k]
        else:
            moovDir = vect[command[0]]
            for k in range(2):
                self.pos[k] += int(command[1:]) * moovDir[k]

    def initP2(self):
        self.pos = [0, 0]
        self.dir = [1, 10]

    def apply2(self, command):
        vect = {
            'N': [1, 0],
            'S': [-1, 0],
            'E': [0, 1],
            'W': [0, -1],
        }
        dirs = [[1.0, 1.0], [1.0, -1.0], [-1.0, -1.0], [-1.0, 1.0]]

        if command[0] in vect:
            moovDir = vect[command[0]]
            for k in range(2):
                self.dir[k] += int(command[1:]) * moovDir[k]

        elif command[0] == 'R':
            numsRotation = int(int(command[1:])/90)
            for rot in range(numsRotation):
                curQuartan = [(-1)**(int(t < 0)) for t in self.dir]
                index = (dirs.index(curQuartan) - 1) % 4
                tmp = self.dir[0]
                self.dir[0] = dirs[index][0] * abs(self.dir[1])
                self.dir[1] = dirs[index][1] * abs(tmp)

        elif command[0] == 'L':
            numsRotation = int(int(command[1:])/90)
            for rot in range(numsRotation):
                curQuartan = [(-1)**(int(t < 0)) for t in self.dir]
                index = (dirs.index(curQuartan) + 1) % 4

                tmp = self.dir[0]
                self.dir[0] = dirs[index][0] * abs(self.dir[1])
                self.dir[1] = dirs[index][1] * abs(tmp)

        elif command[0] == 'F':
            for k in range(2):
                self.pos[k] += int(command[1:]) * self.dir[k]


if __name__ == '__main__':
    start = time.time()

    boat = Boat()

    # Partie 1
    fileIn = open(sys.argv[1])
    for line in fileIn:
        command = line.rstrip()
        #print(boat.pos, "  ", command, "  ", end="")
        boat.apply(command)
        # print(boat.pos)
    print(boat.pos, sum([abs(i) for i in boat.pos]))
    fileIn.close()

    # Partie 2
    boat.initP2()
    fileIn = open(sys.argv[1])
    for line in fileIn:
        command = line.rstrip()
        #print(boat.pos, "  ", command, "  ", end="")
        boat.apply2(command)
        # print(boat.pos)
    print(boat.pos, sum([abs(i) for i in boat.pos]))
    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
