from sys import argv


def fold(grid, axis, level):
    if axis == "y":
        for k in range(len(grid) - level - 1):
            for j in range(len(grid[k])):
                grid[level - k - 1][j] = max((
                    grid[level - k - 1][j],
                    grid[level + k + 1][j]
                ))

        grid = grid[:level]

    elif axis == "x":
        for k in range(len(grid)):
            for j in range(len(grid[-1]) - level - 1):
                grid[k][level - j - 1] = max((
                    grid[k][level + j + 1],
                    grid[k][level - j - 1]
                ))

            grid[k] = grid[k][:level]

    return grid


if __name__ == '__main__':

    dots = []
    dot_part = True
    folds = []

    max_x = 0
    max_y = 0

    input_data = open(argv[1], 'r')
    for line in input_data:
        if line.rstrip("\n") == "":
            dot_part = False
        elif dot_part:
            x = int(line.split(',')[0])
            y = int(line.rstrip('\n').split(',')[1])
            max_x = max((x + 1, max_x))
            max_y = max((y + 1, max_y))
            dots.append((x, y))
        else:
            axis = line.split()[-1][0]
            level = int(line.rstrip("\n").split()[-1].split("=")[-1])
            folds.append((axis, level))
    input_data.close()

    grid = [[0 for i in range(max_x)] for j in range(max_y)]

    for (x, y) in dots:
        grid[y][x] = 1

    for task in folds:
        grid = fold(grid, task[0], task[1])
        print("Part 1 : ", sum([sum(g) for g in grid]))

    for g in grid:
        for e in g:
            if e == 1:
                print("yo", end="")
            else:
                print("  ", end="")
        print()
