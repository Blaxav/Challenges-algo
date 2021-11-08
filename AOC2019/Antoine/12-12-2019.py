from time import time
from copy import deepcopy
from math import gcd
a = time()

def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [Moon(line[1:-2].split(', ')) for line in f.readlines()]

class Moon:
    def __init__(self, coord):
        self.x = int(coord[0][2:])
        self.y = int(coord[1][2:])
        self.z = int(coord[2][2:])
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def __str__(self):
        return str((self.x, self.y, self.z, self.vx, self.vy, self.vz))
    
    def potentialEnergy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
    
    def kineticEnergy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)
    
    def totalEnergy(self):
        return self.potentialEnergy() * self.kineticEnergy()
    
    def coordinates(self):
        return (self.x, self.y, self.z, self.vx, self.vy, self.vz)

def applyGravity(moonsList: list):
    for firstMoon in moonsList:
        for secondMoon in moonsList:
            if firstMoon == secondMoon:
                continue
            else:
                dx = 1 if firstMoon.x < secondMoon.x else -1 if firstMoon.x > secondMoon.x else 0
                dy = 1 if firstMoon.y < secondMoon.y else -1 if firstMoon.y > secondMoon.y else 0
                dz = 1 if firstMoon.z < secondMoon.z else -1 if firstMoon.z > secondMoon.z else 0
            firstMoon.vx += dx
            firstMoon.vy += dy
            firstMoon.vz += dz
    return moonsList

def applyGravityX(moonsList: list):
    for firstMoon in moonsList:
        for secondMoon in moonsList:
            if firstMoon == secondMoon:
                continue
            else:
                dx = 1 if firstMoon.x < secondMoon.x else -1 if firstMoon.x > secondMoon.x else 0
            firstMoon.vx += dx
    return moonsList

def applyGravityY(moonsList: list):
    for firstMoon in moonsList:
        for secondMoon in moonsList:
            if firstMoon == secondMoon:
                continue
            else:
                dy = 1 if firstMoon.y < secondMoon.y else -1 if firstMoon.y > secondMoon.y else 0
            firstMoon.vy += dy
    return moonsList

def applyGravityZ(moonsList: list):
    for firstMoon in moonsList:
        for secondMoon in moonsList:
            if firstMoon == secondMoon:
                continue
            else:
                dz = 1 if firstMoon.z < secondMoon.z else -1 if firstMoon.z > secondMoon.z else 0
            firstMoon.vz += dz
    return moonsList

def applyVelocity(moonsList: list):
    for moon in moonsList:
        moon.x += moon.vx
        moon.y += moon.vy
        moon.z += moon.vz
    return moonsList

def applyVelocityX(moonsList: list):
    for moon in moonsList:
        moon.x += moon.vx
    return moonsList

def applyVelocityY(moonsList: list):
    for moon in moonsList:
        moon.y += moon.vy
    return moonsList

def applyVelocityZ(moonsList: list):
    for moon in moonsList:
        moon.z += moon.vz
    return moonsList

def twoMoonsListsAreEqualsOnX(firstMoonList: list, secondMoonList: list):
    res = True
    for i in range(len(firstMoonList)):
        if firstMoonList[i].x != secondMoonList[i].x or firstMoonList[i].vx != secondMoonList[i].vx:
            res = False
    return res

def twoMoonsListsAreEqualsOnY(firstMoonList: list, secondMoonList: list):
    res = True
    for i in range(len(firstMoonList)):
        if firstMoonList[i].y != secondMoonList[i].y or firstMoonList[i].vy != secondMoonList[i].vy:
            res = False
    return res

def twoMoonsListsAreEqualsOnZ(firstMoonList: list, secondMoonList: list):
    res = True
    for i in range(len(firstMoonList)):
        if firstMoonList[i].z != secondMoonList[i].z or firstMoonList[i].vz != secondMoonList[i].vz:
            res = False
    return res

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def part1(moonsList: list, steps: int):
    for i in range(steps):
        moonsList = applyVelocity(applyGravity(moonsList))
    totalEnergy = 0
    for moon in moonsList:
        totalEnergy += moon.totalEnergy()
    return totalEnergy
            
def part2(moonsList: list):
    initialList = readFile()
    moonsList = applyVelocityX(applyGravityX(moonsList))
    compX = 1
    while not twoMoonsListsAreEqualsOnX(initialList, moonsList):
        moonsList = applyVelocityX(applyGravityX(moonsList))
        compX += 1
    
    moonsList = applyVelocityY(applyGravityY(moonsList))
    compY = 1
    while not twoMoonsListsAreEqualsOnY(initialList, moonsList):
        moonsList = applyVelocityY(applyGravityY(moonsList))
        compY += 1
    
    moonsList = applyVelocityZ(applyGravityZ(moonsList))
    compZ = 1
    while not twoMoonsListsAreEqualsOnZ(initialList, moonsList):
        moonsList = applyVelocityZ(applyGravityZ(moonsList))
        compZ += 1
    return lcm(lcm(compX, compY), compZ)


if __name__ == "__main__":
    vals = readFile()
    steps = 1000
    p1 = part1(vals, steps)
    print(f"Part 1: {p1}")
    vals = readFile()
    p2 = part2(vals)
    print(f"Part 2: {p2}")
    print(time()-a)

