import time
from math import sqrt

from utils import prime_numbers


def read_input(pathToFile):
    l = []
    inputfile = open(pathToFile)
    for line in inputfile:
        l.append([int(i) for i in line.split()])
    return l


def path_val(path, inst):
    t = len(inst)
    return sum([inst[i][path[i]] for i in range(len(path)) ] )

if __name__ == '__main__' :
    start = time.time()

    l = read_input("input_67.txt")
    dyna = []
    for step in l :
        dyna.append([0] * len(step))
        #initialisation du mec
        if len(step) == 1:
            dyna[-1][0] = step[0]
        else :
            dyna[-1][0] = step[0] + dyna[-2][0]
            for i in range(1, len(step)-1):
                dyna[-1][i] = max([dyna[-2][i-1], dyna[-2][i]]) + step[i]
            dyna[-1][-1] = step[-1] + dyna[-2][-1]
        
    

    print("Result: ", max(dyna[-1]))

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
