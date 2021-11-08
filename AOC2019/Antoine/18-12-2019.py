from time import time
from math import inf
from collections import deque, defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def factorizeScheme(scheme: list):
    # On modifie le fichier d'entrée
    height, width = len(scheme), len(scheme[0])
    scheme[height//2 - 1] = scheme[height//2 - 1][:width // 2 - 1] + '@#@' + scheme[height//2 - 1][-width//2 + 2:]
    scheme[height//2] = scheme[height//2][:width // 2 - 1] + '###' + scheme[height//2][-width//2 + 2:]
    scheme[height//2 + 1] = scheme[height//2 + 1][:width // 2 - 1] + '@#@' + scheme[height//2 + 1][-width//2 + 2:]
    # On factorise le labyrinthe en 4 labyrinthes
    firstMaze = [scheme[it][:width // 2 + 1] for it in range(height // 2 + 1)]
    secondMaze = [scheme[it][-width // 2:] for it in range(height // 2 + 1)]
    thirdMaze = [scheme[it][:width // 2 + 1] for it in range(height // 2, height)]
    fourthMaze = [scheme[it][-width // 2:] for it in range(height // 2, height)]
    return [firstMaze, secondMaze, thirdMaze, fourthMaze]


def getAdjacentCases(coord: tuple, scheme: list):
    # On renvoie les 4 cases adjacentes à la case actuelle, dans l'ordre : G, D, B, H
    # return (scheme[row][col-1], scheme[row][col+1], scheme[row-1][col], scheme[row+1][col])
    # On renvoie les coordonnées des cases adjacentes à la case actuelle si elle ne contiennent pas un mur
    row, col = coord
    adjacentCases = list()
    if scheme[row][col-1] != '#':
        adjacentCases.append((row, col-1))
    if scheme[row][col+1] != '#':
        adjacentCases.append((row, col+1))
    if scheme[row-1][col] != '#':
        adjacentCases.append((row-1, col))
    if scheme[row+1][col] != '#':
        adjacentCases.append((row+1, col))
    return adjacentCases

def parseScheme(scheme: list):
    # On parcourt la liste contenant, l'input
    # Dans un premier temps on récolte tous les noeuds : clés, portes et bifurcations
    nodes = dict()
    crossNodeInd = 0
    for row, line in enumerate(scheme):
        for col, char in enumerate(line):
            if char == ".":
                if len(getAdjacentCases((row, col), scheme)) >= 3:
                    nodes[crossNodeInd] = (row, col)
                    crossNodeInd += 1
            elif char != '#':
                nodes[char] = (row, col)
    inverseNodes = {k:v for v, k in nodes.items()}

    # Dans un second temps, on va parcourir cette liste de noeuds pour déterminer les plus proches
    # voisins de chaque noeud
    neighbours = {k:dict() for k in nodes}
    for node, coord in nodes.items():
        initialAdjCases = getAdjacentCases(coord, scheme)
        research = {k:initialAdjCases[k] for k in range(len(initialAdjCases))}
        distance = 1
        explorated = [coord]
        for num in research:
            keepGoing = True
            while keepGoing:
                pathCoord = research[num]
                if pathCoord in nodes.values(): # Si on rencontre une clé
                    neighbours[node][inverseNodes[pathCoord]] = distance
                    keepGoing = False
                    distance = 1
                elif len(getAdjacentCases(pathCoord, scheme)) == 1: # Cul de sac
                    keepGoing = False
                    distance = 1
                else:
                    explorated.append(pathCoord)
                    distance += 1
                    for possibility in getAdjacentCases(pathCoord, scheme):
                        if possibility not in explorated:
                            research[num] = possibility
    return nodes, neighbours

def dijkstra(nodes: dict, neighbours: dict):
    keys = ['@'] + sorted([a for a in nodes if str(a).islower()], key=str.lower)
    distanceMatrix = dict()
    doors = {a:None for a in keys if a.islower()}

    for firstKey in keys:
        remainingNodes = [a for a in nodes if a != firstKey]
        distances = {a:inf for a in nodes}
        for elem in neighbours[firstKey]:
            distances[elem] = neighbours[firstKey][elem]
            if firstKey == '@':
                doors[elem] = ['@'] 
        exploratedNodes = list(firstKey)

        while remainingNodes:
            
            graphNeighbours = {k:v for exploratedNode in exploratedNodes for k, v in neighbours[exploratedNode].items() if k not in exploratedNodes}
            closestNeighbour = min(graphNeighbours, key=graphNeighbours.get)
            for neighbour in neighbours[closestNeighbour]:
                if distances[neighbour] > distances[closestNeighbour] + neighbours[closestNeighbour][neighbour]:
                    distances[neighbour] = distances[closestNeighbour] + neighbours[closestNeighbour][neighbour]
                    if firstKey == '@':
                        doors[neighbour] = doors[closestNeighbour] + [closestNeighbour]


            exploratedNodes.append(closestNeighbour)
            remainingNodes.remove(closestNeighbour)
        distanceMatrix[firstKey] = {k:distances[k] for k in keys if k != firstKey and k.islower()}
    distanceMatrix = {k:v for k, v in distanceMatrix.items() if v}
    doors = {k:[a.lower() for a in v if str(a).isupper()] for k,v in doors.items() if str(k).islower()}
    return distanceMatrix, doors

class Tree:
    def __init__(self, nodes, distanceMatrix, doors, firstNodes):
        # Données du problème
        self.keys = [a for a in nodes if str(a).islower()]
        self.distanceMatrix = distanceMatrix
        self.doors = doors
        self.states = defaultdict(lambda:inf)
        # Données relatives à l'arbre
        self.bestValue = inf
        self.openNodes = deque([Node(0, firstNodes, firstNodes)])
        self.firstNodes = firstNodes
    
    def expandTree(self):
        currentNode = self.openNodes.pop()
        if len(currentNode.path) - sum(len(elem) for elem in self.firstNodes) == len(self.keys) and currentNode.length < self.bestValue:
            self.bestValue = currentNode.length
        else:
            for son in currentNode.reachableKeys(self):
                if son.length < self.bestValue:
                    if son.length < self.states[son.state]:
                        self.states[son.state] = son.length
                        self.openNodes.append(son)


class Node:
    def __init__(self, length, path, key):
        self.length = length
        self.path = path
        self.key = key
        self.state = (key, ''.join(sorted(self.path)))   
    
    def reachableKeys(self, tree):
        for current in self.key:
            if current in tree.distanceMatrix:
                reachable = deque([a for a in tree.distanceMatrix[current] if a not in self.path and not [b for b in tree.doors[a] if b not in self.path]])
                for potentialSon in reachable:
                    if not [a for a in reachable if a != potentialSon and tree.distanceMatrix[current][a] + tree.distanceMatrix[a][potentialSon] == tree.distanceMatrix[current][potentialSon]]:
                        length = self.length + tree.distanceMatrix[current][potentialSon]
                        path = self.path + potentialSon
                        key = self.key.replace(current, potentialSon)
                        yield Node(length, path, key)


def part1():
    scheme = readFile()
    nodes, neighbours = parseScheme(scheme)
    matrix, doors = dijkstra(nodes, neighbours)
    tree = Tree(nodes, matrix, doors, '@')
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp

def part2():
    scheme = readFile()
    mazes = factorizeScheme(scheme)
    matrix, doors, nodes = dict(), dict(), dict()
    newDeps = '@?!$'
    for num, maze in enumerate(mazes, 0):
        tempNodes, neighbours = parseScheme(maze)
        tempMatrix, tempDoors = dijkstra(tempNodes, neighbours)
        tempMatrix[newDeps[num]] = tempMatrix.pop('@')
        matrix.update(tempMatrix)
        doors.update(tempDoors)
        nodes.update(tempNodes)
    tree = Tree(nodes, matrix, doors, newDeps)
    comp = 0
    while tree.openNodes:
        tree.expandTree()
        comp += 1
    return tree.bestValue, comp
        
if __name__ == "__main__":
    p1 = part1()
    print(f"Part 1: {p1[0]} in {p1[1]} iterations")
    p2 = part2()
    print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    print(time()-a)

