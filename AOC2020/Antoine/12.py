from time import time
from math import cos, sin, radians
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[i.strip()[0], int(i.strip()[1:])] for i in f.readlines()]

def treatInstruction(command: str, amplitude: int, direction: str, north: int, east: int):
    angleAndDirection = {0 : 'E', 90: 'N', 180: 'W', 270: 'S', 'E': 0, 'N': 90, 'W': 180, 'S': 270}
    if command == 'F':
        command = angleAndDirection[direction]
    if command == 'N':
        north += amplitude
    elif command == 'S':
        north -= amplitude
    elif command == 'E':
        east += amplitude
    elif command == 'W':
        east -= amplitude
    elif command == 'L':
        direction = (direction+amplitude)%360
    else:
        direction = (direction-amplitude)%360
    
    return direction, north, east

def treatInstructionWaypoint(command: str, amplitude: int, northShip: int, eastShip: int, northWaypoint: int, eastWaypoint: int):
    if command == 'R':
        command, amplitude = 'L', 360 - amplitude
    if command == 'N':
        northWaypoint += amplitude
    elif command == 'S':
        northWaypoint -= amplitude
    elif command == 'E':
        eastWaypoint += amplitude
    elif command == 'W':
        eastWaypoint -= amplitude
    elif command == 'L':
        angle = radians(amplitude)
        eastWaypoint, northWaypoint = eastWaypoint * cos(angle) - northWaypoint * sin(angle), eastWaypoint * sin(angle) + northWaypoint * cos(angle)
    else:
        eastShip += amplitude * eastWaypoint
        northShip += amplitude * northWaypoint

    return northShip, eastShip, northWaypoint, eastWaypoint

def part1(scheme: list):
    direction, north, east = 0, 0, 0
    for command, amplitude in scheme:
        direction, north, east = treatInstruction(command, amplitude, direction, north, east)
    return abs(north)+abs(east)

def part2(scheme: list):
    northShip, eastShip, northWaypoint, eastWaypoint = 0, 0, 1, 10
    for command, amplitude in scheme:
        northShip, eastShip, northWaypoint, eastWaypoint = treatInstructionWaypoint(command, amplitude, northShip, eastShip, northWaypoint, eastWaypoint)
    return int(abs(northShip)+abs(eastShip))

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

