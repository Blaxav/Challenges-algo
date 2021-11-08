from time import time
import unittest
from itertools import combinations
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def parseInput(scheme: list):
    boss, weapons, armors, rings = dict(), dict(), dict(), dict()
    weaponsCount, armorsCount, ringsCount = 0, 0, 0
    for num, line in enumerate(scheme):
        line = line.split()
        if 0 <= num <= 2:
            boss[line[0][:-1]] = int(line[1])
        elif 3 <= num <= 7:
            weapons[weaponsCount] = {'cost': int(line[1]), 'damage': int(line[2]), 'armor': int(line[3])}
            weaponsCount += 1
        elif 8 <= num <= 13:
            armors[armorsCount] = {'cost': int(line[1]), 'damage': int(line[2]), 'armor': int(line[3])}
            armorsCount += 1
        else:
            rings[ringsCount] = {'cost': int(line[1]), 'damage': int(line[2]), 'armor': int(line[3])}
            ringsCount += 1
    return boss, weapons, armors, rings

def gameWon(boss: dict, littleHenry: dict):
    turnsToKillBoss = boss['HitPoints'] // max(1, littleHenry['damage'] - boss['armor'])
    turnsToKillHenry = littleHenry['HitPoints'] // max(1, boss['damage'] - littleHenry['armor'])
    return turnsToKillBoss <= turnsToKillHenry

def part1(scheme: list):
    boss, weapons, armors, rings = parseInput(scheme)
    littleHenry = {k:0 for k in boss}
    littleHenry['HitPoints'], littleHenry['cost'] = 100, 0
    costs = []
    for weapon in range(5):
        for armor in range(6):
            littleHenry['damage'] += weapons[weapon]['damage']
            littleHenry['armor'] += armors[armor]['armor']
            littleHenry['cost'] += weapons[weapon]['cost'] + armors[armor]['cost']
            if gameWon(boss, littleHenry):
                costs.append(littleHenry['cost'])
            littleHenry['damage'], littleHenry['armor'], littleHenry['cost'] = 0, 0, 0
            for ring in range(6):
                littleHenry['damage'] += rings[ring]['damage'] + weapons[weapon]['damage']
                littleHenry['armor'] += rings[ring]['armor'] + armors[armor]['armor']
                littleHenry['cost'] += rings[ring]['cost'] + weapons[weapon]['cost'] + armors[armor]['cost'] 
                if gameWon(boss, littleHenry):
                    costs.append(littleHenry['cost'])
                littleHenry['damage'], littleHenry['armor'], littleHenry['cost'] = 0, 0, 0
            for ring in combinations(range(6), 2):
                littleHenry['damage'] += rings[ring[0]]['damage'] + rings[ring[1]]['damage'] + weapons[weapon]['damage']
                littleHenry['armor'] += rings[ring[0]]['armor'] + rings[ring[1]]['armor'] + armors[armor]['armor']
                littleHenry['cost'] += rings[ring[0]]['cost'] + rings[ring[1]]['cost'] + weapons[weapon]['cost'] + armors[armor]['cost'] 
                if gameWon(boss, littleHenry):
                    costs.append(littleHenry['cost'])
                littleHenry['damage'], littleHenry['armor'], littleHenry['cost'] = 0, 0, 0
    return min(costs)

def gameLost(boss: dict, littleHenry: dict):
    turnsToKillBoss = boss['HitPoints'] // max(1, littleHenry['damage'] - boss['armor'])
    turnsToKillHenry = littleHenry['HitPoints'] // max(1, boss['damage'] - littleHenry['armor'])
    return turnsToKillBoss > turnsToKillHenry

def part2(scheme: list):
    boss, weapons, armors, rings = parseInput(scheme)
    littleHenry = {k:0 for k in boss}
    littleHenry['HitPoints'], littleHenry['cost'] = 100, 0
    costs = []
    for weapon in range(5):
        for armor in range(6):
            littleHenry['damage'] += weapons[weapon]['damage']
            littleHenry['armor'] += armors[armor]['armor']
            littleHenry['cost'] += weapons[weapon]['cost'] + armors[armor]['cost']
            if gameLost(boss, littleHenry):
                costs.append(littleHenry['cost'])
            littleHenry['damage'], littleHenry['armor'], littleHenry['cost'] = 0, 0, 0
            for ring in range(6):
                littleHenry['damage'] += rings[ring]['damage'] + weapons[weapon]['damage']
                littleHenry['armor'] += rings[ring]['armor'] + armors[armor]['armor']
                littleHenry['cost'] += rings[ring]['cost'] + weapons[weapon]['cost'] + armors[armor]['cost'] 
                if gameLost(boss, littleHenry):
                    costs.append(littleHenry['cost'])
                littleHenry['damage'], littleHenry['armor'], littleHenry['cost'] = 0, 0, 0
            for ring in combinations(range(6), 2):
                littleHenry['damage'] += rings[ring[0]]['damage'] + rings[ring[1]]['damage'] + weapons[weapon]['damage']
                littleHenry['armor'] += rings[ring[0]]['armor'] + rings[ring[1]]['armor'] + armors[armor]['armor']
                littleHenry['cost'] += rings[ring[0]]['cost'] + rings[ring[1]]['cost'] + weapons[weapon]['cost'] + armors[armor]['cost'] 
                if gameLost(boss, littleHenry):
                    costs.append(littleHenry['cost'])
                littleHenry['damage'], littleHenry['armor'], littleHenry['cost'] = 0, 0, 0
    return max(costs)

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

