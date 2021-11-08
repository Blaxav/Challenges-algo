def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

def mass_to_fuel(mass):
    return max(mass//3 - 2, 0)

def part1(numberList: list):
    return [mass_to_fuel(elem) for elem in numberList]

def part2(numberList: list):
    res = 0
    while sum(numberList) > 0:
        res += sum(part1(numberList))
        numberList = part1(numberList)
    return res

if __name__ == "__main__":
    vals = readFile()
    print(vals)
    p1 = part1(vals)
    print(f"Part 1: {sum(p1)}")
    p2 = part2(vals)
    print(f"Part 2: {p2}")