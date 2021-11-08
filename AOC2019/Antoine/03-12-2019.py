def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [Wire(str(num)[:-1].split(",")) for num in f.readlines()]

class Wire:
    def __init__(self, input):
        self.input = input
        self.points = {(0, 0) : 0}
        self.__initPoints()

    def __initPoints(self):
        x, y, step = 0, 0, 0
        for segment in self.input:
            direction, norm = segment[0], int(segment[1:])
            dx = 1 if direction == "R" else -1 if direction == "L" else 0
            dy = 1 if direction == "U" else -1 if direction == "D" else 0
            for point in range(norm):
                x += dx
                y += dy
                step += 1
                if (x, y) not in self.points.keys():
                    self.points[(x, y)] = step
        del self.points[(0,0)]

def getIntersection(firstWire, secondWire):
    return set(firstWire.points.keys()).intersection(set(secondWire.points.keys()))

def part1(vals:list):
    intersection = getIntersection(vals[0], vals[1])
    manhattanValues = [abs(elem[0]) + abs(elem[1]) for elem in intersection]
    return min(manhattanValues)

def part2(vals: list):
    intersection = getIntersection(vals[0], vals[1])
    stepsList = [vals[0].points[elem] + vals[1].points[elem] for elem in intersection]
    return min(stepsList)


if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")