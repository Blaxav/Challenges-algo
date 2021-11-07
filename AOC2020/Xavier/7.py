import re
import sys
import time
from collections import defaultdict
#from functools import lru_cache
from math import sqrt

from utils import add_one, is_prime, prime_numbers


########################################################################################
# part 1
########################################################################################
def part1(instance):

    fileIn = open(instance)
    containedIn = defaultdict( set )

    for line in fileIn:
        k = 0
        for color in re.finditer('\w+ \w+ bag?', line):
            colorName = color.group().split("bag")[0].rstrip()
            if k == 0:
                container = colorName
            else:
                containedIn[colorName].add(container)

            k += 1
    fileIn.close()
    
    newContainers = containedIn["shiny gold"].copy()
    containersNextIte = set()
    containersOfShiny = containedIn["shiny gold"].copy()
    total = 0
    while len(newContainers) > 0:
        total += len(newContainers)
        for v in newContainers:
            for cont in containedIn[v]:
                if cont not in containersOfShiny:
                    containersNextIte.add(cont)
                    containersOfShiny.add(cont)
        newContainers.clear()
        newContainers = containersNextIte.copy()
        containersNextIte.clear()

    print("Result: ", len(containersOfShiny) )

########################################################################################
# part 2 : en recursif avec un cache
########################################################################################
#@lru_cache(maxsize = None)
def bag_value(bagName, neighbors):
    
    if len(neighbors[bagName]) == 0:
        return 1
    else:
        total = 0
        for bag in neighbors[bagName]:
            total += (neighbors[bagName][bag] * bag_value(bag, neighbors) )
        total += 1
        return total


def part2(instance):
    fileIn = open(instance)
    neighbors = {}

    for line in fileIn:
        k = 0
        for color in re.finditer('\d*\s*\w+ \w+ bag?', line):

            colorline = color.group().split("bag")[0].rstrip()
            if k == 0:
                container = colorline
                neighbors[container] = {}
            else:
                number, color = colorline.split()[0], " ".join(colorline.split()[1:])
                
                if number != "no":
                    neighbors[container][color] = int(number)
            
            k += 1
    fileIn.close()

    print("Part 2: ", bag_value("shiny gold", neighbors) - 1 )

########################################################################################
# main
########################################################################################
if __name__ == '__main__' :
    start = time.time()

    instance = sys.argv[1]

    part1(instance)
    
    part2(instance)

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
