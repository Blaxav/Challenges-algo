from time import time
import unittest
from collections import defaultdict, deque
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def splitInstructions(scheme: list):
    return [a for a in scheme if "goes" in a], [a for a in scheme if "gives" in a]

def treatGoesInstructions(bots: dict, goesInstructions: list):
    for instruction in goesInstructions:
        value, bot = (int(s) for s in instruction.split() if s.isdigit())
        if len(bots[bot]) == 1 and value < bots[bot][0]:
            bots[bot].appendleft(value)
        else:
            bots[bot].append(value)

    return bots

def assignValues(bots: dict, outputs: dict, values: list, giverBot: int):
    assignedValues = [bots[giverBot].popleft(), bots[giverBot].popleft()]
    resBot = 0
    if assignedValues == [17, 61]:
        resBot = giverBot
    for it in range(2):
        if values[it+2] == "output":
            outputs[values[it]] = assignedValues[it]
        else:
            if len(bots[values[it]]) == 1 and assignedValues[it] < bots[values[it]][0]:
                bots[values[it]].appendleft(assignedValues[it])
            else:
                bots[values[it]].append(assignedValues[it]) 

    return bots, outputs, resBot

def treatGivesInstructions(bots: dict, outputs: dict, givesInstructions: list):
    givesValues = dict()
    for instruction in givesInstructions:
        giverBot, lowReceiver, highReceiver = (int(s) for s in instruction.split() if s.isdigit())
        lowReceiverType, highReceiverType = (s for s in instruction[4:].split() if s in ["output", "bot"])
        givesValues[giverBot] = [lowReceiver, highReceiver, lowReceiverType, highReceiverType]

    while givesValues:
        fullBots = [k for k, v in bots.items() if len(v) == 2]
        for fullBot in fullBots:
            bots, outputs, resBot = assignValues(bots, outputs, givesValues[fullBot], fullBot)
            if resBot:
                resultP1 = resBot
            del givesValues[fullBot]

    resultP2 = outputs[0] * outputs[1] * outputs[2]

    return resultP1, resultP2

def part1(scheme: list):
    goesInstructions, givesInstructions = splitInstructions(scheme)
    bots, outputs = defaultdict(deque), dict()
    bots = treatGoesInstructions(bots, goesInstructions)
    res = treatGivesInstructions(bots, outputs, givesInstructions)

    return res

def part2(scheme: list):
    goesInstructions, givesInstructions = splitInstructions(scheme)
    bots, outputs = defaultdict(deque), dict()
    bots = treatGoesInstructions(bots, goesInstructions)
    res = treatGivesInstructions(bots, outputs, givesInstructions)

    return res

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1[0]}")
    p2 = part2(scheme)
    print(f"Part 2: {p2[1]}")
    print(time()-a)

