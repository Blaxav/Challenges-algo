from time import time
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def newPosition(x: int, y:int, char: str):
    if char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    elif char == '<':
        x -= 1
    elif char == '>':
        x += 1
    return (x, y)

def part1():
    scheme = readFile()
    x, y = 0, 0
    deliveredHouses = [(x, y)]
    for char in scheme:
        x, y = newPosition(x, y, char)
        deliveredHouses.append((x, y))
    return len(set(deliveredHouses))

def splitRoads(scheme: str):
    return [scheme[i] for i in range(len(scheme)) if i % 2 == 0], [scheme[i] for i in range(len(scheme)) if i % 2 == 1]

def part2():
    scheme = readFile()
    santaRoad, robotRoad = splitRoads(scheme)
    x, y = 0, 0
    deliveredHouses = [(x, y)]
    for char in santaRoad:
        x, y = newPosition(x, y, char)
        deliveredHouses.append((x, y))
    x, y = 0, 0
    for char in robotRoad:
        x, y = newPosition(x, y, char)
        deliveredHouses.append((x, y))
    return len(set(deliveredHouses))

if __name__ == "__main__":
    p1 = part1()
    print(f"Part 1: {p1}")
    p2 = part2()
    print(f"Part 2: {p2}")
    print(time()-a)