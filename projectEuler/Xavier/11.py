import time
from utils import prime_numbers
from math import sqrt

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print("%-4i" % (grid[i][j]), end="")
        print()

def read():
    grid = []
    input = open("input_11.txt")
    for line in input :
        grid.append([])
        for elt in line.split():
            grid[-1].append(int(elt))
    
    print_grid(grid)
    return grid

if __name__ == '__main__' :
    start = time.time()

    grid = read()
    N = len(grid)

    prod = 0
    result = 0

    print("TAille: " , N)
    # Diago
    for i in range(N-3):
        M = len(grid[i])
        for j in range(M-3):
            #print("        ", i, j, result, grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3], grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3])
            if grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3] > result :
                result = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
                print(("Diago   ", i, j, grid[i][j], result))

    # Diago 2
    for i in range(N-3):
        M = len(grid[i])
        for j in range(3, N):
            print("        ", i, j, result, grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3], grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3])
            if grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3] > result :
                result = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
                print(("Diago   ", i, j, grid[i][j], result))

    # Right
    for i in range(N):
        M = len(grid[i])
        for j in range(M-3):
            #print("        ", i, j, result, grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3], grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3])
            if grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3] > result :
                result = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
                print(("Right  ", i, j, grid[i][j],  result))

    # Down
    for i in range(N-3):
        M = len(grid[i])
        for j in range(M):
            #print("        ", i, j, result, grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j], grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j])
            if grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j] > result:
                result = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
                print(("Down  ", i, j, grid[i][j], result))

    print("Result: ", result)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))