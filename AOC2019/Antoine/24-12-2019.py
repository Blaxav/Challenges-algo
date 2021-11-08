from time import time
a = time()

def read_map(file) -> list:
    with open(file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def count_bugs_in_row(grid: list, row: int) -> int:
    return ''.join(grid[row]).count('#')


def count_bugs_in_col(grid: list, col: int) -> int:
    return sum([1 if row[col] == '#' else 0 for row in grid])


def count_bugs_in_deeper_level(grids: dict, level: int, line: int, col: int, size: int) -> int:
    if line == 1 and col == 2:  # top
        return count_bugs_in_row(grids[level + 1], 0)
    elif line == 2 and col == 3:  # right
        return count_bugs_in_col(grids[level + 1], size - 1)
    elif line == 3 and col == 2:  # bottom
        return count_bugs_in_row(grids[level + 1], size - 1)
    elif line == 2 and col == 1:
        return count_bugs_in_col(grids[level + 1], 0)


def has_bug_in_outer_level(grids: dict, level: int, x: int, y: int, size: int):
    return (x < 0 and grids[level - 1][2][1] == '#') \
           or (x >= size and grids[level - 1][2][3] == '#') \
           or (y < 0 and grids[level - 1][1][2] == '#') \
           or (y >= size and grids[level - 1][3][2] == '#')


def is_middle(x: int, y: int, size: int) -> bool:
    return x == size // 2 and y == size // 2


def count_adj_bugs(grids: dict, level: int, line: int, col: int, is_recursive_grid=False) -> int:
    count = 0
    grid = grids[level]
    size = len(grid)
    if is_recursive_grid and (grids.get(level + 1) is None or grids.get(level - 1) is None):
        return 0
    for dxy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        x = col + dxy[0]
        y = line + dxy[1]
        if 0 <= x < size and 0 <= y < size:
            if is_recursive_grid and is_middle(x, y, size):
                count += count_bugs_in_deeper_level(grids, level, line, col, size)
            else:
                count += 1 if grid[y][x] == '#' else 0
        elif is_recursive_grid and has_bug_in_outer_level(grids, level, x, y, size):
            count += 1
    return count


def serialize_state(grid: list) -> str:
    res = []
    for line in grid:
        res.append(''.join(line))
    return ''.join(res)


def get_empty_grid(size: int) -> list:
    grid = []
    for i in range(size):
        grid.append(['.'] * size)
    return grid


def has_life(grids: dict, level: int, x: int, y: int, is_recursive_grid=False) -> bool:
    adj_bugs = count_adj_bugs(grids, level, y, x, is_recursive_grid)
    return (grids[level][y][x] == '#' and adj_bugs == 1) \
           or (grids[level][y][x] == '.' and (adj_bugs == 1 or adj_bugs == 2))


def simulate(grids: dict, is_recursive_grid=False) -> dict:
    new_grids = {}
    for level, grid in grids.items():
        size = len(grid)
        new_grid = get_empty_grid(size)
        for y in range(size):
            for x in range(size):
                if is_recursive_grid and is_middle(x, y, size):
                    continue
                if has_life(grids, level, x, y, is_recursive_grid):
                    new_grid[y][x] = '#'
        new_grids[level] = new_grid
    return new_grids


def calc_biodiversity_rating(serial_state: str) -> int:
    biodiversity_rating = 0
    for i, val in enumerate(list(serial_state)):
        if val == '#':
            biodiversity_rating += 2 ** i
    return biodiversity_rating


def part1(filename: str) -> int:
    grid = read_map(filename)
    grids = {0: grid}
    states = {serialize_state(grid)}
    while True:
        grids = simulate(grids)
        state = serialize_state(grids[0])
        if state in states:
            return calc_biodiversity_rating(state)
        states.add(state)


def count_bugs(grids: dict) -> int:
    return sum([serialize_state(grid).count('#') for grid in grids.values()])


def part2(filename: str, minutes: int) -> int:
    grid = read_map(filename)
    size = len(grid)
    grids = {0: grid}
    # We need to allocate minutes/2 levels up and minutes/2 levels down, plus 2 extra boundary levels.
    for m in range(1, (minutes // 2) + 2):
        grids[m] = get_empty_grid(size)
        grids[-m] = get_empty_grid(size)
    for m in range(minutes):
        grids = simulate(grids, True)
    return count_bugs(grids)

if __name__ == "__main__":
    p1 = part1('24-12-2019-input.txt')
    print(f"Part 1: {p1}")
    p2 = part2('24-12-2019-input.txt', 200)
    print(f"Part 2: {p2}")
    print(time()-a)