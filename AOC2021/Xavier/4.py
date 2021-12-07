from sys import argv


class Grid(list):
    def __init__(self):
        list.__init__(self)
        # the grid contains a list checked of zeros
        # set to one when the number is checked
        self.checked = []
        self.n = 0
        self.m = 0

    def add_line(self, line):
        self.append([int(i) for i in line.rstrip("\n").split()])
        self.checked.append([0] * len(line.split()))
        self.n += 1
        self.m = len(line.split())

    def check(self, val):
        for i in range(self.n):
            for j in range(self.m):
                if self[i][j] == val:
                    self.checked[i][j] = 1
                    return

    def win(self):
        # check in lines
        for i in range(self.n):
            if sum(self.checked[i]) == self.m:
                return True

        # check in columns
        for j in range(self.m):
            if sum([self.checked[i][j] for i in range(self.n)]) == self.n:
                return True

        return False

    def unmark_numbers(self):
        result = []
        for i in range(self.n):
            for j in range(self.m):
                if not self.checked[i][j]:
                    result.append(self[i][j])
        return result


if __name__ == '__main__':

    # Grid is a list of each grid
    grids = []

    # bingo_draw is the random drawing of numbers
    bingo_draw = []

    # Read input
    input_data = open(argv[1], 'r')
    grid_part = False
    for line in input_data:
        if not grid_part:
            bingo_draw = [int(i) for i in line.rstrip("\n").split(',')]
            grid_part = True
        else:
            if line.rstrip("\n") == "":
                # New grid
                grids.append(Grid())
            else:
                grids[-1].add_line(line)
    input_data.close()

    # Game
    winners = [0] * len(grids)
    for val in bingo_draw:
        for g in range(len(grids)):
            grids[g].check(val)

            if grids[g].win():
                print("Winner grid ", g, " ! ")
                print("Part 1 : ", sum(grids[g].unmark_numbers()) * val)
                winners[g] = 1

                if sum(winners) == len(grids):
                    exit()
