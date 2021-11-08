def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return Constellation({str(elem)[4:7]:str(elem)[:3] for elem in f.readlines()})

class Constellation:
    def __init__(self, input):
        self.input = input
        self.orbits = {'COM' : 0}
        self.__initOrbits()

    def __initOrbits(self):
        orbitsList = self.input.keys()
        for orbit in orbitsList:
            distance = 0
            parent = orbit
            while parent not in self.orbits.keys():
                parent = self.input[parent]
                distance += 1
            self.orbits[orbit] = distance + self.orbits[parent]

def getParents(constellation, orbit):
    parentsList = ['COM']
    parent = constellation.input[orbit]
    while parent != 'COM':
        parentsList.append(parent)
        parent = constellation.input[parent]
    return parentsList


def part1(constellation):
    return sum(constellation.orbits.values())

def part2(constellation):
    parentsOfYou = getParents(constellation, 'YOU')
    parentsOfSan = getParents(constellation, 'SAN')
    commonPath = set(parentsOfYou).intersection(set(parentsOfSan))
    return len(parentsOfSan) + len(parentsOfYou) - 2 * len(commonPath) 

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")