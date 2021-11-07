from collections import deque
from sys import displayhook


class Policy:
    def __init__(self, policy, cost, playerLife, bossLife, mana, spellsTurnsLeft):
        self.policy = policy
        self.playerLife = playerLife
        self.bossLife = bossLife
        self.spellsTurnsLeft = spellsTurnsLeft
        self.cost = cost
        self.mana = mana

    def addTurn(self, id, spells, bossAtk, lifeLost):
        # Losing life at the beginning
        self.playerLife -= lifeLost
        if self.playerLife <= 0:
            return False

        # 1. Apllying casts effects
        for k in range(len(spells)):
            if self.spellsTurnsLeft[k] > 0:
                self.bossLife -= spells[k].damage
                self.mana += spells[k].manaHeal

                self.spellsTurnsLeft[k] -= 1

        # 2. Apllying player turn
        self.policy.append(id)
        self.cost += spells[id].cost
        self.mana -= spells[id].cost
        if self.spellsTurnsLeft[id] > 0 or self.mana < 0:
            return False  # Returns False if the policy is unaplicable
            # Or not enough mana either spell already active
        self.spellsTurnsLeft[id] += spells[id].turns

        # 3. Applying casts effect
        activeDef = 0
        for k in range(len(spells)):
            if self.spellsTurnsLeft[k] > 0:
                self.bossLife -= spells[k].damage
                self.mana += spells[k].manaHeal
                self.playerLife += spells[k].heal
                activeDef += spells[k].shield
                self.spellsTurnsLeft[k] -= 1

        # 4. applying boss turn
        self.playerLife -= max([1, bossAtk - activeDef])

        return True

    def playerDead(self):
        return self.playerLife <= 0

    def bossDead(self):
        return self.bossLife <= 0

    def display(self):
        print("Player life : ", self.playerLife)
        print("Boss life   : ", self.bossLife)
        print("Policy      : ", self.policy)
        print("Total cost  : ", self.cost)
        print("Mana left   : ", self.mana)
        print()

    def copy(self):
        return Policy([i for i in self.policy], self.cost, self.playerLife, self.bossLife, self.mana, [i for i in self.spellsTurnsLeft])


class Spell:
    def __init__(self, cost, damage, heal, shield, manaHeal, turns):
        self.damage = damage
        self.heal = heal
        self.shield = shield
        self.manaHeal = manaHeal
        self.turns = turns
        self.cost = cost


if __name__ == '__main__':

    boss = {
        "PV": 51,
        "damage": 9
    }

    spells = [
        Spell(53, 4, 0, 0, 0, 1),
        Spell(73, 2, 2, 0, 0, 1),
        Spell(113, 0, 0, 7, 0, 6),
        Spell(173, 3, 0, 0, 0, 6),
        Spell(229, 0, 0, 0, 101, 5)
    ]

    nSpells = len(spells)

    player = {
        "PV": 50,
        "mana": 500
    }

    # brut force
    policy = Policy([], 0, player["PV"], boss["PV"],
                    player["mana"], [0] * nSpells)

    policy.display()

    it = 0
    survivingPolicies = deque([policy])
    best_policy = []
    best_cost = 1e9
    while survivingPolicies:
        policy = survivingPolicies.popleft()
        if policy.cost < (best_cost - 53 - 1):
            for k in range(nSpells):
                newPolicy = policy.copy()
                if newPolicy.addTurn(k, spells, boss["damage"], 0):
                    if newPolicy.bossDead():
                        best_cost = min([best_cost, newPolicy.cost])
                        print(newPolicy.policy, "  ", newPolicy.cost,
                              "  **** BOSS DEAD ****")
                    elif not newPolicy.playerDead():
                        survivingPolicies.append(newPolicy)

    print("Part1 : ", best_cost)

    # brut force
    policy = Policy([], 0, player["PV"], boss["PV"],
                    player["mana"], [0] * nSpells)

    it = 0
    survivingPolicies = deque([policy])
    best_policy = []
    best_cost = 1e9
    while survivingPolicies:
        policy = survivingPolicies.popleft()
        if policy.cost < (best_cost - 53 - 1):
            for k in range(nSpells):
                newPolicy = policy.copy()
                if newPolicy.addTurn(k, spells, boss["damage"], 1):
                    if newPolicy.bossDead():
                        best_cost = min([best_cost, newPolicy.cost])
                        print(newPolicy.policy, "  ", newPolicy.cost,
                              "  **** BOSS DEAD ****")
                    elif not newPolicy.playerDead():
                        survivingPolicies.append(newPolicy)

    print("Part2 : ", best_cost)
