from time import time
from collections import deque
import re
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]


def solveCalculusLeftToRight(calculus: str):
    calculus = calculus.replace(' ', '')
    numbers, operands = deque([int(elem) for elem in re.split('\+|\*', calculus)]), deque([elem for elem in re.split(r'\d+', calculus) if elem])
    while operands:
        number1 = numbers.popleft()
        number2 = numbers.popleft()
        operand = operands.popleft()
        if operand == '+':
            numbers.appendleft(number1+number2)
        else:
            numbers.appendleft(number1*number2)
    
    return numbers[0]

def solveCalculusSumThenProduct(calculus: str):
    calculus = calculus.replace(' ', '')
    numbers, operands = [int(elem) for elem in re.split('\+|\*', calculus)], [elem for elem in re.split(r'\d+', calculus) if elem]
    result = 1
    while '+' in operands:
        ind = operands.index('+')
        numbers[ind] = numbers[ind] + numbers[ind+1]
        operands.remove('+')
        del numbers[ind+1]
    
    for number in numbers:
        result *= number
    
    return result


def solveCalculus(calculus: str, part: int):
    while '(' in calculus:
        groups = re.findall('\(([^()]+)\)', calculus)
        for group in groups:
            calculus = calculus.replace('(' + group + ')', str(solveCalculusLeftToRight(group))) if part == 1 else calculus.replace('(' + group + ')', str(solveCalculusSumThenProduct(group)))
    
    return solveCalculusLeftToRight(calculus) if part == 1 else solveCalculusSumThenProduct(calculus)
         
def part1(scheme: list):
    totalSum = 0
    for calculus in scheme:
        totalSum += solveCalculus(calculus, 1)
    return totalSum

def part2(scheme: list):
    totalSum = 0
    for calculus in scheme:
        totalSum += solveCalculus(calculus, 2)
    return totalSum

class Tests(unittest.TestCase):

    def test(self):
        self.assertEqual(solveCalculusLeftToRight('1 + 2 * 3 + 4 * 5 + 6'), 71)
        self.assertEqual(solveCalculus('1 + (2 * 3) + (4 * (5 + 6))', 1), 51)
        self.assertEqual(solveCalculus('2 * 3 + (4 * 5)', 1), 26)
        self.assertEqual(solveCalculus('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1), 437)
        self.assertEqual(solveCalculus('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 1), 12240)
        self.assertEqual(solveCalculus('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 1), 13632)
        self.assertEqual(solveCalculus('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 2), 23340)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

