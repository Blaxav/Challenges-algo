from time import time
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def calculateSurface(dimensions: str):
    sepDim = [int(a) for a in dimensions.split('x')]
    sepDim.sort()
    return int(2 * (1.5*sepDim[0]*sepDim[1] + sepDim[0]*sepDim[2] + sepDim[1]*sepDim[2]))

def part1():
    scheme = readFile()
    return sum(calculateSurface(a) for a in scheme)

def smallestPerimeter(dimensions: str):
    sepDim = [int(a) for a in dimensions.split('x')]
    sepDim.sort()
    return 2 * (sepDim[0] + sepDim[1])

def volume(dimensions: str):
    sepDim = [int(a) for a in dimensions.split('x')]
    return sepDim[0] * sepDim[1] * sepDim[2]


def part2():
    scheme = readFile()
    return sum(smallestPerimeter(a) + volume(a) for a in scheme)

if __name__ == "__main__":
    p1 = part1()
    print(f"Part 1: {p1}")
    p2 = part2()
    print(f"Part 2: {p2}")
    print(time()-a)