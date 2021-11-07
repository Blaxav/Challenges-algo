
def findPosition(n):
    k, maxElt = findSquareNumber(n)
    position = [k, -k]  # coordinates on the grid

    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    side = 0

    # print(maxElt, "  ", position)

    while True:
        if maxElt - 2*(k) > n:
            maxElt -= 2*(k)
            position[0] += 2*k*direction[side][0]
            position[1] += 2*k*direction[side][1]
            # print(maxElt, "  ", position)
            side += 1
        else:
            position[0] += (maxElt - n)*direction[side][0]
            position[1] += (maxElt - n)*direction[side][1]
            break

    return position


def findSquareNumber(n):
    # 1. in which square is n
    squareSize = 1
    sideLength = 1
    maxElt = 1
    k = 1
    while maxElt < n:
        k += 1
        sideLength += 2
        squareSize = 4*(sideLength - 1)
        maxElt += squareSize

    return (k-1, maxElt)


def computeCurrentValue(grid, x, y):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i, j) != (0, 0):
                grid[x][y] += grid[x+i][y + j]


if __name__ == '__main__':

    n = 312051
    print(n, "  ", findPosition(n))
    print("Part 1 :", sum([abs(i) for i in findPosition(n)]))

    #print(5678941254789563, "  ", findPosition(5678941254789563))

    grid = []
    gridSize = 1001
    x = 500  # position of the 1 on a 1001*1001 grid
    y = 500
    for k in range(gridSize):
        grid.append([0] * gridSize)

    grid[x][y] = 1  # initialization

    direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    side = 0

    currentSquare = 0

    while True:
        print("NEW SQUARE")
        currentSquare += 1

        # init current square
        x += 1
        computeCurrentValue(grid, x, y)
        print((x, y, grid[x][y]))

        for side in range(4):
            step = 2*currentSquare + 1*(side > 0)
            #print(currentSquare, "  ", step)
            for it in range(step-1):
                x += direction[side][0]
                y += direction[side][1]
                computeCurrentValue(grid, x, y)
                print((x, y, grid[x][y]))

                if grid[x][y] > n:
                    print("Value ", grid[x][y])
                    exit()
