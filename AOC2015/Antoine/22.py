from time import time
import unittest
from math import inf
from collections import deque
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def parseInput(scheme: list):
    spells = dict()
    for line in scheme:
        line = line.split()
        spells[int(line[0])] = {'manaCost': int(line[1]), 'directDamage': int(line[2]), 'heal': int(line[3]), 'armor': int(line[4]), 'armorTurn': int(line[5]), 'poison': int(line[6]), 'poisonTurn': int(line[7]), 'mana': int(line[8]), 'manaTurn': int(line[9])}
    return spells
# Sorts :
# 0 : missile
# 1 : vol de vie
# 2 : armure
# 3 : poison
# 4 : mana
class Node:
    def __init__(self, henryHP: int, henryMana: int, henryUsedMana: int, bossHP: int, bossDamage:int, remainingShield: int, remainingPoison: int, remainingMana: int, spell: int, usedSpells: str):
        self.henryHP = henryHP
        self.henryMana = henryMana
        self.henryUsedMana = henryUsedMana
        self.bossHP = bossHP
        self.bossDamage = bossDamage
        self.remainingShield = remainingShield
        self.remainingPoison = remainingPoison
        self.remainingMana = remainingMana
        self.spell = spell
        self.usedSpells = usedSpells + str(spell)
    
    def __str__(self):
        return str(self.henryHP)
    
    def possibleNodes(self, spells):
        possibilities = []
        if self.henryMana >= spells[0]['manaCost']:
            possibilities.append(0)
        if self.henryMana >= spells[1]['manaCost']:
            possibilities.append(1)
        if self.remainingShield in [0,1] and self.henryMana >= spells[2]['manaCost']:
            possibilities.append(2)
        if self.remainingPoison in [0,1] and self.henryMana >= spells[3]['manaCost']:
            possibilities.append(3)
        if self.remainingMana in [0,1] and self.henryMana >= spells[4]['manaCost']:
            possibilities.append(4)
        for spell in possibilities:
            yield Node(self.henryHP, self.henryMana, self.henryUsedMana, self.bossHP, self.bossDamage, self.remainingShield, self.remainingPoison, self.remainingMana, spell, self.usedSpells)
    
    def henryTurn(self, spells: dict, hard=False):
        if hard:
            self.henryHP -= 1
        # Effets du poison et du mana
        self.bossHP -= spells[3]['poison']*min(self.remainingPoison, 1)
        self.henryMana += spells[4]['mana']*min(self.remainingMana, 1)
        # Réduction du timer des sorts de durée
        self.remainingPoison = max(self.remainingPoison-1, 0)
        self.remainingMana = max(self.remainingMana-1, 0)
        self.remainingShield = max(self.remainingShield-1, 0)
        # Rechargement des sorts de durée
        self.remainingShield += spells[self.spell]['armorTurn']
        self.remainingPoison += spells[self.spell]['poisonTurn']
        self.remainingMana += spells[self.spell]['manaTurn']
        # Effets du sort d'attaque
        self.bossHP -= spells[self.spell]['directDamage']
        self.henryHP += spells[self.spell]['heal']
        self.henryMana -= spells[self.spell]['manaCost']
        self.henryUsedMana += spells[self.spell]['manaCost']
    
    def bossTurn(self, spells: dict, hard=False):
        if hard:
            self.henryHP -= 1
        # Effets du poison et du mana
        self.bossHP -= spells[3]['poison']*min(self.remainingPoison, 1)
        self.henryMana += spells[4]['mana']*min(self.remainingMana, 1)
        # Réduction du timer des sorts de durée
        self.remainingPoison = max(self.remainingPoison-1, 0)
        self.remainingMana = max(self.remainingMana-1, 0)
        self.remainingShield = max(self.remainingShield-1, 0)
        # Attaque du boss
        if self.bossHP > 0:
            self.henryHP -= self.bossDamage - spells[2]['armor']*min(self.remainingShield, 1)
        
def part1(scheme: list):
    spells = parseInput(scheme)
    bestValue = inf
    openNodes = deque([])
    for spell in range(5):
        openNodes.append(Node(50, 500, 0, 58, 9, 0, 0, 0, spell, ''))
    while openNodes:
        currentNode = openNodes.pop()
        currentNode.henryTurn(spells)
        if currentNode.bossHP <= 0:
            if currentNode.henryUsedMana < bestValue:
                bestValue = currentNode.henryUsedMana
                print(0, currentNode.usedSpells, bestValue, currentNode.henryHP, currentNode.bossHP)
            continue
        currentNode.bossTurn(spells)
        if currentNode.bossHP <= 0:
            if currentNode.henryUsedMana < bestValue:
                bestValue = currentNode.henryUsedMana
                print(1, currentNode.usedSpells, bestValue, currentNode.henryHP, currentNode.bossHP)
            continue
        if currentNode.henryHP <= 0:
            continue
        for son in currentNode.possibleNodes(spells):
            if son.henryUsedMana < bestValue:
                openNodes.append(son)
    return bestValue

def part2(scheme: list):
    spells = parseInput(scheme)
    bestValue = inf
    openNodes = deque([])
    for spell in range(5):
        openNodes.append(Node(50, 500, 0, 58, 9, 0, 0, 0, spell, ''))
    while openNodes:
        currentNode = openNodes.pop()
        currentNode.henryTurn(spells, True)
        if currentNode.bossHP <= 0:
            if currentNode.henryUsedMana < bestValue:
                bestValue = currentNode.henryUsedMana
                print(0, currentNode.usedSpells, bestValue, currentNode.henryHP, currentNode.bossHP)
            continue
        currentNode.bossTurn(spells, True)
        if currentNode.bossHP <= 0:
            if currentNode.henryUsedMana < bestValue:
                bestValue = currentNode.henryUsedMana
                print(1, currentNode.usedSpells, bestValue, currentNode.henryHP, currentNode.bossHP)
            continue
        if currentNode.henryHP <= 0:
            continue
        for son in currentNode.possibleNodes(spells):
            if son.henryUsedMana < bestValue:
                openNodes.append(son)
    return bestValue

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

