def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [int(num) for num in f.readline().split("-")]

def separateDigits(number: int):
    return [(number // 10**a) % 10 for a in reversed(range(6))]

def adjacentValues(numberList: list):
    for i in range(len(numberList) - 1):
        if numberList[i] == numberList[i+1]:
            return True
    return False

def growingValues(numberList: list):
    for i in range(len(numberList) - 1):
        if numberList[i] > numberList[i+1]:
            return False
    return True

def adjacentValuesStrict(numberList: list):
    for i in range(len(numberList) - 1):
        if numberList[i] == numberList[i+1] and numberList.count(numberList[i]) == 2:
            return True
    return False

def part1(vals: list):
    validNumbers = set()
    for number in range(vals[0], vals[1] + 1):
        numberList = separateDigits(number)
        if len(numberList) == 6 and adjacentValues(numberList) and growingValues(numberList):
            validNumbers.add(number)
    return len(validNumbers)

def part2(vals: list):
    validNumbers = set()
    for number in range(vals[0], vals[1] + 1):
        numberList = separateDigits(number)
        if len(numberList) == 6 and adjacentValuesStrict(numberList) and growingValues(numberList):
            validNumbers.add(number)
    return len(validNumbers)
            
if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")