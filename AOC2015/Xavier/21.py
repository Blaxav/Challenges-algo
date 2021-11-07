import sys
from itertools import combinations
from math import ceil


class FightObject:
    def __init__(self, atk, defense, cost):
        self.atk = atk
        self.defense = defense
        self.cost = cost


class Magasin:
    def __init__(self):
        self.weapons = []
        self.armors = []
        self.ringAtk = []
        self.ringDef = []

    def fill(self, path_to_data):
        input_data = open(sys.argv[1], 'r')
        category = ""
        for line in input_data:
            if line == '\n':
                pass
            elif line.split()[0] == "Weapons:":
                category = "weapons"
            elif line.split()[0] == "Armor:":
                category = "armors"
            elif line.split()[0] == "Rings:":
                category = "rings"
            else:
                self.addObject(category, line)

        input_data.close()

    def addObject(self, category, line):
        if category == "weapons":
            self.addWeapon(line)
        elif category == "armors":
            self.addArmor(line)
        elif category == "rings":
            if line.split()[0] == "Damage":
                self.addRingAtk(line)
            else:
                self.addRingDef(line)

    def addWeapon(self, line):
        self.weapons.append(FightObject(
            int(line.split()[2]), 0, int(line.split()[1])))

    def addArmor(self, line):
        self.armors.append(FightObject(
            0, int(line.split()[3]), int(line.split()[1])))

    def addRingAtk(self, line):
        self.ringAtk.append(FightObject(
            int(line.split()[3]), 0, int(line.split()[2])))

    def addRingDef(self, line):
        self.ringDef.append(FightObject(
            0, int(line.split()[4]), int(line.split()[2])))


class AttackSet:
    def __init__(self, atk, cost, pv, defense, nRings):
        self.damages = max([1, atk - defense])
        self.cost = cost
        self.turns_to_kill = ceil(pv / self.damages)
        self.nRings = nRings


if __name__ == '__main__':

    boss = {
        "PV": int(sys.argv[2]),
        "damage": int(sys.argv[3]),
        "armor": int(sys.argv[4])
    }

    store = Magasin()
    store.fill(sys.argv[1])

    # Computing every possible attack set
    attackSets = []
    for weap in store.weapons:
        for nRings in range(3):
            for rings in combinations(store.ringAtk, nRings):
                atk = weap.atk + sum([r.atk for r in rings])
                cost = weap.cost + sum([r.cost for r in rings])
                attackSets.append(
                    AttackSet(atk, cost, boss["PV"], boss["armor"], nRings))

    # Computing every possible defense set
    # A defense set is computed like an attakSet of the boss, reducing its attack with
    # the player PV's
    # Adding the NULL Armor as no armor is possible
    defenseSets = []
    for armor in store.armors + [FightObject(0, 0, 0)]:
        for nRings in range(3):
            for rings in combinations(store.ringDef, nRings):
                defense = armor.defense + sum([r.defense for r in rings])
                cost = armor.cost + sum([r.cost for r in rings])
                defenseSets.append(
                    AttackSet(boss["damage"], cost, 100, defense, nRings))

    for atkset in attackSets:
        print("%-10i%-10i%-10i" %
              (atkset.damages, atkset.cost, atkset.turns_to_kill))

    print()
    for defset in defenseSets:
        print("%-10i%-10i%-10i" %
              (defset.damages, defset.cost, defset.turns_to_kill))

    best_cost = 1e9
    for atkSet in attackSets:
        for defSet in defenseSets:
            # atkSet turns to kill : number of turn to kill boss
            # defSet turns to kill : number of turn to be killed
            if atkSet.turns_to_kill <= defSet.turns_to_kill:
                # Check set validity
                if atkSet.nRings + defSet.nRings <= 2:
                    best_cost = min([best_cost, atkSet.cost + defSet.cost])
    print("Part1 : ", best_cost)

    best_cost = 0
    for atkSet in attackSets:
        for defSet in defenseSets:
            # atkSet turns to kill : number of turn to kill boss
            # defSet turns to kill : number of turn to be killed
            if atkSet.turns_to_kill > defSet.turns_to_kill:
                # Check set validity
                if atkSet.nRings + defSet.nRings <= 2:
                    best_cost = max([best_cost, atkSet.cost + defSet.cost])
    print("Part2 : ", best_cost)
