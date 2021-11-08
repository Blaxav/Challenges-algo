from time import time
from collections import defaultdict, deque
from math import inf
from copy import deepcopy
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [i.replace('\n', '') for i in f.readlines()]

def getAdjacentCases(coord: tuple, scheme: list):
    # On renvoie les 4 cases adjacentes à la case actuelle
    row, col = coord
    adjacentCases = dict()
    if scheme[row][col-1] not in ['#', ' ']:
        adjacentCases[scheme[row][col-1]] = (row, col-1)
    if scheme[row][col+1] not in ['#', ' ']:
        adjacentCases[scheme[row][col+1]] = (row, col+1)
    if scheme[row-1][col] not in ['#', ' ']:
        adjacentCases[scheme[row-1][col]] = (row-1, col)
    if scheme[row+1][col] not in ['#', ' ']:
        adjacentCases[scheme[row+1][col]] = (row+1, col)
    return adjacentCases

def isCrossNode(coord: tuple, scheme: list):
    row, col = coord
    adjacentCases = list()
    if scheme[row][col-1] == '.':
        adjacentCases.append((row, col-1))
    if scheme[row][col+1] == '.':
        adjacentCases.append((row, col+1))
    if scheme[row-1][col] == '.':
        adjacentCases.append((row-1, col))
    if scheme[row+1][col] == '.':
        adjacentCases.append((row+1, col))
    return adjacentCases

def parseScheme(scheme: list):
    # On parcourt la liste contenant, l'input
    # Dans un premier temps on récolte tous les noeuds
    nodes = dict()
    crossNodeInd = 0
    for row, line in enumerate(scheme):
        if row in (0, len(scheme)-1):
            continue
        for col, char in enumerate(line):
            if col in (0, len(line)-1):
                continue
            if char.isupper():
                adjacentCases = getAdjacentCases((row, col), scheme)
                if len(adjacentCases) == 2:
                    items = sorted(list(adjacentCases.keys()))
                    teleport = ''.join(sorted(char+items[1]))
                    if teleport in ['AA', 'ZZ']:
                        nodes[teleport] = adjacentCases[items[0]]
                    elif row in [1, len(scheme)-2] or col in [1, len(line)-2]:
                        nodes['o'+teleport] = adjacentCases[items[0]]
                    else:
                        nodes['i'+teleport] = adjacentCases[items[0]]
            if char == "." and len(isCrossNode((row, col), scheme)) >= 3:
                nodes[crossNodeInd]= (row, col)
                crossNodeInd += 1
    return nodes

def getNeighbours(nodes: dict, scheme: list):
    coordToNode = {v:k for k, v in nodes.items()}
    neighbours = {k:dict() for k in nodes}
    for node, coord in nodes.items():
        if isinstance(node, str):
            explorated = list()
            explorated.append(coord)
            newCoord, distance, keepGoing = isCrossNode(coord, scheme)[0], 1, True
            while keepGoing:
                if newCoord in coordToNode:
                    neighbours[node], keepGoing = {coordToNode[newCoord]: distance}, False
                elif len(isCrossNode(newCoord, scheme)) == 1:
                    keepGoing = False
                else:
                    explorated.append(newCoord)
                    for elem in isCrossNode(newCoord, scheme):
                        if elem not in explorated:
                            newCoord = elem
                            distance += 1
            if len(node) == 3:
                num = 'o' if node[0] == 'i' else 'i'
                neighbours[node][num+node[1:]] = 1
        else:
            explorated = list()
            explorated.append(coord)
            for adjacentCase in isCrossNode(coord, scheme):
                newCoord, distance, keepGoing = adjacentCase, 1, True
                while keepGoing:
                    if newCoord in coordToNode:
                        neighbours[node][coordToNode[newCoord]] = distance
                        keepGoing = False
                    elif len(isCrossNode(newCoord, scheme)) == 1:
                        keepGoing = False
                    else:
                        explorated.append(newCoord)
                        for elem in isCrossNode(newCoord, scheme):
                            if elem not in explorated:
                                newCoord = elem
                                distance += 1 
    return neighbours

def research(neighbours: dict, firstNode: str):
    openNodes = deque([firstNode])
    distances = defaultdict(lambda:inf)
    distances[firstNode] = 0
    comp = 0
    bestValue = inf
    while openNodes:
        currentNode = openNodes.popleft()
        for son, val in neighbours[currentNode[1]].items():
            comp += 1
            sonState = currentNode[:1] + (son,)
            if distances[currentNode] + val < min(bestValue, distances[sonState]):
                if sonState == (0, 'ZZ'):
                    bestValue = distances[currentNode] + val
                distances[sonState] = distances[currentNode] + val
                openNodes.append(sonState)
    return bestValue, comp

def makeInnerOuterScheme(scheme: list, nodes: dict):
    outerScheme, innerScheme = deepcopy(scheme), deepcopy(scheme)
    outerGen = (v for k,v in nodes.items() if str(k).startswith('o'))
    innerGen = (v for k,v in nodes.items() if k == 'AA' or k == 'ZZ')
    for row, col in outerGen:
        outerScheme[row] = outerScheme[row][:col] + '#' + outerScheme[row][col+1:]
    for row, col in innerGen:
        innerScheme[row] = innerScheme[row][:col] + '#' + innerScheme[row][col+1:]
    return innerScheme, outerScheme

def generateSonState(currentLayer: int, currentNode: str, son: str):
    if str(currentNode).startswith('i') and son == 'o' + str(currentNode)[1:]:
        return (currentLayer+1, son)
    elif str(currentNode).startswith('o') and son == 'i' + str(currentNode)[1:]:
        return (currentLayer-1, son)
    else:
        return (currentLayer, son)

def researchWithLayers(innerNeighbours: dict, outerNeighbours: dict, firstState: str):
    openStates = deque([firstState])
    distances = defaultdict(lambda:inf)
    parents = dict()
    distances[firstState] = 0
    comp = 0
    bestValue = inf
    while openStates:
        currentState = openStates.popleft()
        currentLayer, currentNode = currentState
        neighbours = outerNeighbours if currentLayer == 0 else innerNeighbours
        for son, val in neighbours[currentNode].items():
            comp += 1
            sonState = generateSonState(currentLayer, currentNode, son)
            if distances[currentState] + val < min(bestValue, distances[sonState]):
                if sonState == (0, 'ZZ'):
                    bestValue = distances[currentState] + val
                parents[sonState] = currentState
                distances[sonState] = distances[currentState] + val
                openStates.append(sonState)
    return bestValue, comp, parents, distances

def part1():
    scheme = readFile()
    nodes = parseScheme(scheme)
    neighbours = getNeighbours(nodes, scheme)    
    bestValue, comp = research(neighbours, (0,'AA'))
    return bestValue, comp

def generatePath(parents: dict, state: tuple):
    path, parent = [state], None
    while parent != (0, 'AA'):
        parent = parents[path[len(path)-1]]
        path.append(parent)
    path = [a for a in path if isinstance(a[1], str)]
    return path[::-1]

def part2():
    scheme = readFile()
    nodes = parseScheme(scheme)
    innerScheme, outerScheme = makeInnerOuterScheme(scheme, nodes)
    innerNodes, outerNodes = parseScheme(innerScheme), parseScheme(outerScheme)
    innerNeighbours, outerNeighbours = getNeighbours(innerNodes, innerScheme), getNeighbours(outerNodes, outerScheme)
    bestValue, comp, parents, distances = researchWithLayers(innerNeighbours, outerNeighbours, (0, 'AA'))
    return bestValue, comp

if __name__ == "__main__":
    p1 = part1()
    print(f"Part 1: {p1[0]} in {p1[1]} iterations")
    p2 = part2()
    print(f"Part 2: {p2[0]} in {p2[1]} iterations")
    print(time()-a)