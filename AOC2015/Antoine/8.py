from time import time
import unittest
import re
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]    

def countMemory(line: str):
    line = line[1:-1]
    line = line.replace('\\\\', 'x')
    line = line.replace('\\\"', 'x')
    line, _ = re.subn('\\\\x..', 'x', line)
    return len(line)

def part1(scheme: list):
    return sum(len(line) - countMemory(line) for line in scheme)

def countEscaped(line: str):
    escaped = line
    escaped = escaped.replace("\\", "\\\\")
    escaped = escaped.replace('"', '\\"')
    escaped = '"' + escaped + '"'
    return len(escaped)

def part2(scheme: list):
    return sum(countEscaped(line) - len(line) for line in scheme)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

