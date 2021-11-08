from time import time
import unittest
from collections import deque
import re
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        tiles = list()
        for line in f.readlines():
            line = line.strip()
            if re.match('^(Tile)', line):
                currentTile = int(line[5:9])
                currentTileBorders = ["", "", "", ""]
                comp = 1
            if re.match('^(#|\.)', line):
                if comp == 1:
                    currentTileBorders[0] += line
                    currentTileBorders[3] += line[0]
                    currentTileBorders[1] += line[-1]
                elif comp == 10:
                    currentTileBorders[2] += line
                    currentTileBorders[3] += line[0]
                    currentTileBorders[1] += line[-1]
                    tiles.append(Tile(currentTile, currentTileBorders[0], currentTileBorders[1], currentTileBorders[2], currentTileBorders[3]))
                    tiles.append(Tile(currentTile, currentTileBorders[3][::-1], currentTileBorders[0], currentTileBorders[1][::-1], currentTileBorders[2]))
                    tiles.append(Tile(currentTile, currentTileBorders[2][::-1], currentTileBorders[3][::-1], currentTileBorders[0][::-1], currentTileBorders[1][::-1]))
                    tiles.append(Tile(currentTile, currentTileBorders[1], currentTileBorders[2][::-1], currentTileBorders[3], currentTileBorders[0][::-1]))
                    tiles.append(Tile(currentTile, currentTileBorders[2], currentTileBorders[1][::-1], currentTileBorders[0], currentTileBorders[3][::-1]))
                    tiles.append(Tile(currentTile, currentTileBorders[3], currentTileBorders[2], currentTileBorders[1], currentTileBorders[0]))
                    tiles.append(Tile(currentTile, currentTileBorders[0][::-1], currentTileBorders[3], currentTileBorders[2][::-1], currentTileBorders[1]))
                    tiles.append(Tile(currentTile, currentTileBorders[1][::-1], currentTileBorders[0][::-1], currentTileBorders[3][::-1], currentTileBorders[2][::-1]))
                else:
                    currentTileBorders[3] += line[0]
                    currentTileBorders[1] += line[-1]
                comp += 1

    return tiles

class Tile:
    def __init__(self, tileId: int, topBorder: str, rightBorder: str, bottomBorder: str, leftBorder: str):
        self.id = tileId
        self.topBorder = sum(pow(2,n)*(1 if a == '#' else 0) for n, a in enumerate(topBorder[::-1]))
        self.rightBorder = sum(pow(2,n)*(1 if a == '#' else 0) for n, a in enumerate(rightBorder[::-1]))
        self.bottomBorder = sum(pow(2,n)*(1 if a == '#' else 0) for n, a in enumerate(bottomBorder[::-1]))
        self.leftBorder = sum(pow(2,n)*(1 if a == '#' else 0) for n, a in enumerate(leftBorder[::-1]))

    def __repr__(self):
        return '-'.join([str(self.id), str(self.topBorder), str(self.rightBorder), str(self.bottomBorder), str(self.leftBorder)])

class Node:
    def __init__(self, order: list, length):
        self.order = order
        self.lastTile = order[-1]
        self.orderLength = len(order)
        self.upperTile = self.order[-length] if self.orderLength >= length else None
        self.storedIds = [elem.id for elem in self.order]
    
    def reachableNodes(self, tiles, length):
        # Définir ici comment rechercher les prochains noeuds
        for tile in tiles:
            if tile.id not in self.storedIds:
                if self.orderLength < length:
                    if tile.leftBorder == self.lastTile.rightBorder:
                        print(tile.id)
                        yield Node(self.order+[tile], length)
                elif self.orderLength % length == 0:
                    if tile.topBorder == self.upperTile.bottomBorder:
                        yield Node(self.order+[tile], length)
                else:
                    if tile.leftBorder == self.lastTile.rightBorder and tile.topBorder == self.upperTile.bottomBorder: 
                        yield Node(self.order+[tile], length)

class Tree:
    def __init__(self, firstNode, tiles):
        # Données relatives à l'arbre
        self.openNodes = deque([firstNode])
        self.firstNode = firstNode
        # Données du problèmes
        self.tiles = tiles
        self.length = len(tiles) // 8
        self.result = 0
    
    def expandTree(self):
        currentNode = self.openNodes.pop() # .pop() -> profondeur, .popleft() -> largeur
        for son in currentNode.reachableNodes(self.tiles, self.length):
            if son.orderLength == pow(self.length, 2):
                self.result = son.order[0].id * son.order[self.length-1].id * son.order[-self.length].id * son.order[-1].id
            else:
                self.openNodes.append(son)
            
def part1(scheme: list):
    for elem in scheme:
        if elem.id in [1951, 2311]:
            print(elem)

    # length = len(scheme) // 8
    # for tile in scheme:
    #     firstNode = Node([tile], length)
    #     tree = Tree(firstNode, scheme)
    #     while tree.openNodes:
    #         tree.expandTree()
    #         if tree.result != 0:
    #             return tree.result

def part2(scheme: list):
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

