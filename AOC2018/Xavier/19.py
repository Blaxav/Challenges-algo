from collections import defaultdict, deque
from sys import argv


class Grid:
    def __init__(self):
        self.lines = []

    def at(self, pos):
        if pos.y < 0 or pos.y >= len(self.lines):
            return ' '
        if pos.x < 0 or pos.x >= len(self.lines[pos.y]):
            return ' '
        return self.lines[pos.y][pos.x]

    def add(self, line):
        self.lines.append(line.rstrip("\n"))

    def __str__(self):
        return "\n".join(self.lines)


class Position:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.y, self.x)

    def __add__(self, p):
        return Position(self.y + p.y, self.x + p.x)

    def __sub__(self, p):
        return Position(self.y - p.y, self.x - p.x)

    def __ne__(self, p):
        return (self.x != p.x) or (self.y != p.y)


if __name__ == '__main__':

    grid = Grid()
    input_data = open(argv[1], 'r')
    for line in input_data:
        grid.add(line)
    input_data.close()

    # Init : search laby entrance
    pos = Position(0, 0)
    for i in range(len(grid.lines[0])):
        if grid.at(Position(0, i)) == "|":
            pos.x = i
            break

    print("Init : ", pos.y, "   ", pos.x, "   ", grid.at(pos))

    result = []
    direction = Position(1, 0)

    # Define the 4 possible directions
    vectors = [
        Position(0, 1),
        Position(0, -1),
        Position(1, 0),
        Position(-1, 0)
    ]
    steps = 0

    while grid.at(pos) != ' ':
        steps += 1
        if grid.at(pos) == "+":
            for d in [v for v in vectors if v != direction and v != (Position(0, 0) - direction)]:
                if grid.at(pos + d) != ' ':
                    pos += d
                    direction = d
                    break
        else:
            if grid.at(pos) not in ['-', '|', '+']:
                result += grid.at(pos)
            pos += direction

    print("Part 1 : ", "".join(result))
    print("Part 2 : ", steps)
