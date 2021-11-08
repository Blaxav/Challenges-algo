from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def toggle(state: list, coords: list):
    for row in range(coords[0], coords[2]+1):
        for col in range(coords[1], coords[3]+1):
            state[row][col] = not state[row][col]
    return state

def turnOn(state: list, coords: list):
    for row in range(coords[0], coords[2]+1):
        for col in range(coords[1], coords[3]+1):
            state[row][col] = True
    return state

def turnOff(state: list, coords: list):
    for row in range(coords[0], coords[2]+1):
        for col in range(coords[1], coords[3]+1):
            state[row][col] = False
    return state

def evoluteLights(instruction: str, state: list):
    instruction = instruction.replace(' through ', ',')
    if instruction.startswith('toggle'):
        instruction = instruction.replace('toggle ', '')
        coords = [int(a) for a in instruction.split(',')]
        return toggle(state, coords)
    if instruction.startswith('turn on'):
        instruction = instruction.replace('turn on ', '')
        coords = [int(a) for a in instruction.split(',')]
        return turnOn(state, coords)
    if instruction.startswith('turn off'):
        instruction = instruction.replace('turn off ', '')
        coords = [int(a) for a in instruction.split(',')]
        return turnOff(state, coords)

def countTrue(state: list):
    return sum(len([a for a in line if a == True]) for line in state)

def part1(scheme: list):
    state = [[False]*1000 for it in range(1000)]
    for instruction in scheme:
        state = evoluteLights(instruction, state)
    return countTrue(state)

def toggleBrightness(state: list, coords: list):
    for row in range(coords[0], coords[2]+1):
        for col in range(coords[1], coords[3]+1):
            state[row][col] += 2
    return state

def turnOnBrightness(state: list, coords: list):
    for row in range(coords[0], coords[2]+1):
        for col in range(coords[1], coords[3]+1):
            state[row][col] += 1
    return state

def turnOffBrightness(state: list, coords: list):
    for row in range(coords[0], coords[2]+1):
        for col in range(coords[1], coords[3]+1):
            state[row][col] = max(0, state[row][col]-1)
    return state

def evoluteBrightness(instruction: str, state: list):
    instruction = instruction.replace(' through ', ',')
    if instruction.startswith('toggle'):
        instruction = instruction.replace('toggle ', '')
        coords = [int(a) for a in instruction.split(',')]
        return toggleBrightness(state, coords)
    if instruction.startswith('turn on'):
        instruction = instruction.replace('turn on ', '')
        coords = [int(a) for a in instruction.split(',')]
        return turnOnBrightness(state, coords)
    if instruction.startswith('turn off'):
        instruction = instruction.replace('turn off ', '')
        coords = [int(a) for a in instruction.split(',')]
        return turnOffBrightness(state, coords)

def countBrightness(state: list):
    return sum(sum(line) for line in state)

def part2(scheme: list):
    state = [[0]*1000 for it in range(1000)]
    for instruction in scheme:
        state = evoluteBrightness(instruction, state)
    return countBrightness(state)

class Tests(unittest.TestCase):

    def testLights(self):
        state = [[False]*1000 for it in range(1000)]
        self.assertEqual(countTrue(state), 0)
        state = evoluteLights('turn on 0,0 through 999,999', state)
        self.assertEqual(countTrue(state), 1_000_000)
        state = evoluteLights('toggle 0,0 through 999,0', state)
        self.assertEqual(countTrue(state), 999_000)
        state = evoluteLights('turn off 499,499 through 500,500', state)
        self.assertEqual(countTrue(state), 998_996)
    
    def testBrightness(self):
        state = [[0]*1000 for it in range(1000)]
        self.assertEqual(countBrightness(state), 0)
        state = evoluteBrightness('turn on 0,0 through 0,0', state)
        self.assertEqual(countBrightness(state), 1)
        state = evoluteBrightness('toggle 0,0 through 999,999', state)
        self.assertEqual(countBrightness(state), 2_000_001)
        state = evoluteBrightness('turn off 0,0 through 2,3', state)
        self.assertEqual(countBrightness(state), 1_999_989)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

