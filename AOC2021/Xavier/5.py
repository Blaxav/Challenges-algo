from sys import argv


class Point:
    def __init__(self, coord):
        self.x = int(coord.split(",")[0])
        self.y = int(coord.split(",")[1])

    def __str__(self):
        return str(self.x) + "," + str(self.y)


class Segment:
    def __init__(self, p1, p2):
        if  p1.x <= p2.x:
            self.beg = p1
            self.end = p2
        else:
            self.beg = p2
            self.end = p1

    def is_vertical(self):
        if self.beg.x == self.end.x:
            return True
        return False

    def is_horizontal(self):
        if self.beg.y == self.end.y:
            return True
        return False

    def is_diagonal(self):
        return abs(self.beg.x - self.end.x) == abs(self.beg.y - self.end.y)

    def __str__(self):
        return str(self.beg) + " -> " + str(self.end)


if __name__ == '__main__':

    lines = []

    # Read input
    input_data = open(argv[1], 'r')
    for line in input_data:
        first, last = line.rstrip("\n").split("-> ")
        lines.append(Segment(Point(first), Point(last)))

    input_data.close()

    # Creating the grid with max coordinates observed
    max_x = 0
    max_y = 0
    for seg in lines:
        for x in (seg.beg.x, seg.end.x):
            max_x = max((x, max_x))
        for y in (seg.beg.y, seg.end.y):
            max_y = max((y, max_y))

    grid = []
    for k in range(max_y + 1):
        grid.append([0]*(max_x + 1))

    for seg in lines:
        if seg.is_vertical():
            for y in range(seg.beg.y, seg.end.y + 1):
                grid[y][seg.beg.x] += 1
            for y in range(seg.end.y, seg.beg.y + 1):
                grid[y][seg.beg.x] += 1

        if seg.is_horizontal():
            for x in range(seg.beg.x, seg.end.x + 1):
                grid[seg.beg.y][x] += 1
            for x in range(seg.end.x, seg.beg.x + 1):
                grid[seg.beg.y][x] += 1

    total_overlap = 0
    for l in grid:
        for val in l:
            if val >= 2:
                total_overlap += 1
    print("Part 1 : ", total_overlap)

    for seg in lines:
        if seg.is_diagonal():

            if seg.end.y >= seg.beg.y:
                y_sign = +1
            else:
                y_sign = -1

            if seg.end.x >= seg.beg.x:
                x_sign = +1
            else:
                x_sign = -1

            for k in range(0, seg.end.x - seg.beg.x + 1):
                grid[seg.beg.y + (k*y_sign)][seg.beg.x + (k*x_sign)] += 1

    total_overlap = 0
    for l in grid:
        for val in l:
            if val >= 2:
                total_overlap += 1
    print("Part 2 : ", total_overlap)
