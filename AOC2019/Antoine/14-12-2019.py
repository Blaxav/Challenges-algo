from time import time
from math import ceil
a = time()

def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return RecipeBook([(line[:-1].split(" => ")) for line in f.readlines()])


class RecipeBook:
    def __init__(self, input):
        self.input = input
        self.book = dict()
        self.__initBook()

    def __initBook(self):
        self.book = {createRecipe(a)[0]:createRecipe(a)[1] for a in self.input}

def createRecipe(recipe: list):
    react, prod = recipe[0].split(", "), recipe[1].split(" ")
    reactDict = {a.split(" ")[1]:int(a.split(" ")[0]) for a in react}
    prodDict = {'productStoch' : int(prod[0]), 'reactives' : reactDict}
    return prod[1], prodDict

def part1(recipes: dict, stock: dict, chemical: str, quantity: int):
    usedFromStock = min(quantity, stock[chemical])
    quantity += -usedFromStock
    stock[chemical] += -usedFromStock
    cDict = recipes[chemical]
    rDict = cDict['reactives']
    stock[chemical] += (cDict['productStoch'] * ceil(quantity/cDict['productStoch'])) - quantity
    if 'ORE' in rDict:
        return rDict['ORE'] * ceil(quantity/cDict['productStoch'])
    else:
        oreComp = 0
        for reactive in rDict:
            oreComp += part1(recipes, stock, reactive, ceil(quantity/cDict['productStoch']) * rDict[reactive])
        return oreComp

def part2(recipes: dict, stock: dict, chemical: str, quantity: int, oreStock: int, result: int):
    largeAmountWithoutStock = int(oreStock/result)
    firstShot = int((largeAmountWithoutStock/part1(recipes, stock, chemical, largeAmountWithoutStock)) * oreStock)
    while 1:
        stock = {a:0 for a in vals.book}
        test = part1(recipes, stock, chemical, firstShot + 1)
        if test <= oreStock:
            firstShot += 1
        else:
            break
    return firstShot

if __name__ == "__main__":
    vals = readFile()
    stock = {a:0 for a in vals.book}
    p1 = part1(vals.book, stock, 'FUEL', 1)
    print(f"Part 1: {p1}")
    oreStock = 1_000_000_000_000
    stock = {a:0 for a in vals.book}
    p2 = part2(vals.book, stock, 'FUEL', 1, oreStock, p1)
    print(f"Part 2: {p2}")
    print(time()-a)