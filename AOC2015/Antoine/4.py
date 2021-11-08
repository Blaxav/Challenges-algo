from time import time
from hashlib import md5
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def part1():
    comp = 0
    scheme = readFile()
    while not md5((scheme+str(comp)).encode('utf-8')).hexdigest().startswith('00000'):
        comp += 1
    return comp

def part2():
    comp = 0
    scheme = readFile()
    while not md5((scheme+str(comp)).encode('utf-8')).hexdigest().startswith('000000'):
        comp += 1
    return comp

if __name__ == "__main__":
    p1 = part1()
    print(f"Part 1: {p1}")
    p2 = part2()
    print(f"Part 2: {p2}")
    print(time()-a)