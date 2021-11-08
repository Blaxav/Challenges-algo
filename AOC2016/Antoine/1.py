from time import time
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return f.readline().strip().split(', ')

def updatePosition(position: list, direction: str, leftRight: str, length: int):
    if direction == 'N':
        if leftRight == 'L':
            newPosition, newDirection = [position[0]-length, position[1]], 'W'
        if leftRight == 'R':
            newPosition, newDirection = [position[0]+length, position[1]], 'E'
    if direction == 'S':
        if leftRight == 'L':
            newPosition, newDirection = [position[0]+length, position[1]], 'E'
        if leftRight == 'R':
            newPosition, newDirection = [position[0]-length, position[1]], 'W'
    if direction == 'W':
        if leftRight == 'L':
            newPosition, newDirection = [position[0], position[1]-length], 'S'
        if leftRight == 'R':
            newPosition, newDirection = [position[0], position[1]+length], 'N'
    if direction == 'E':
        if leftRight == 'L':
            newPosition, newDirection = [position[0], position[1]+length], 'N'
        if leftRight == 'R':
            newPosition, newDirection = [position[0], position[1]-length], 'S'
    return newPosition, newDirection

def part1(scheme: list):
    position, direction = [0, 0], 'N'
    for elem in scheme:
        leftRight, length = elem[0], int(elem[1:])
        position, direction = updatePosition(position, direction, leftRight, length)
    return sum(abs(i) for i in position)

def part2(scheme: list):
    position, direction = [0, 0], 'N'
    visitedPositions = []
    for elem in scheme:
        leftRight, length = elem[0], int(elem[1:])
        for it in range(length):
            position, newDirection = updatePosition(position, direction, leftRight, 1)
            if position in visitedPositions:
                return sum(abs(i) for i in position)
            else:
                visitedPositions.append(position)
        direction = newDirection

if __name__ == "__main__":
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)