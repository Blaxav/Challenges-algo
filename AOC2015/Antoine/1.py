from time import time
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def part1():
    scheme = readFile()
    return scheme.count('(') - scheme.count(')')

def part2():
    scheme = readFile()
    floor = 0
    for num, char in enumerate(scheme, 1):
        if char == ')':
            floor -= 1
        else:
            floor += 1
        
        if floor < 0:
            return num

if __name__ == "__main__":
    p1 = part1()
    print(f"Part 1: {p1}")
    p2 = part2()
    print(f"Part 2: {p2}")
    print(time()-a)