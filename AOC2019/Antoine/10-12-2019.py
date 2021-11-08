from math import sqrt, atan2, pi


def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

class Asteroid:
    def __init__(self, x: int, y: int, ox: int, oy: int):
        self.x = x
        self.y = y
        self.dist = sqrt((x - ox)**2 + (y - oy)**2)
        self.angle = pi - atan2(x - ox, y - oy)
    
    def __str__(self):
        return str((self.x, self.y, self.dist, self.angle))

def initAsteroidsList(scheme: list, x: int, y: int):
    return [Asteroid(i, j, x, y) for j in range(len(scheme)) 
        for i in range(len(scheme[j])) if scheme[j][i] == "#" and (i, j) != (x, y)]

def getVisibleAsteroidsNumber(scheme: list, x: int, y: int):
    asteroidList = initAsteroidsList(scheme, x, y)
    anglesSet = set([asteroid.angle for asteroid in asteroidList])
    return len(anglesSet)

def part1(scheme: list):
    sx, sy, smax = 0, 0, 0
    for y in range(len(scheme)):
        for x in range(len(scheme[y])):
            if scheme[y][x] == ".":
                continue
            visibleAsteroids = getVisibleAsteroidsNumber(scheme, x, y)
            if visibleAsteroids > smax:
                sx, sy, smax = x, y, visibleAsteroids
    return sx, sy, smax

            
def part2(scheme: list, x: int, y: int, count: int):
    asteroidList = initAsteroidsList(scheme, x, y)
    closestAsteroidDict = dict()
    for asteroid in asteroidList:
        if asteroid.angle in closestAsteroidDict:
            if asteroid.dist < closestAsteroidDict[asteroid.angle].dist:
                closestAsteroidDict[asteroid.angle] = asteroid
        else:
            closestAsteroidDict[asteroid.angle] = asteroid
    closestAsteroidSortedByAngle = sorted(closestAsteroidDict, key= lambda k: closestAsteroidDict[k].angle)
    return closestAsteroidDict[closestAsteroidSortedByAngle[count - 1]]


if __name__ == "__main__":
    vals = readFile()
    p1 = part1(vals)
    print(f"Part 1: {p1[2]}")
    p2 = part2(vals, p1[0], p1[1], 200)
    print(f"Part 2: {p2.x*100 + p2.y}")

