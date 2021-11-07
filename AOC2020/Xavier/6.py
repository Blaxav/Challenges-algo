import re
import time
from math import sqrt

from utils import add_one, is_prime, prime_numbers

if __name__ == '__main__' :
    start = time.time()

    fileIn = open("input_6.txt")

    answers = set()
    total = 0
    for line in fileIn:
        # new group
        if line == "\n":
            total += len(answers)
            answers.clear()
        else :
            for c in line.rstrip():
                answers.add(c)
        
    total += len(answers)
    answers.clear()
    print("Result: ", total)
    fileIn.close()

    fileIn = open("input_6.txt")

    answers = set()
    total = 0
    firstPeople = True
    toRemove = []
    for line in fileIn:
        # new group
        if line == "\n":
            total += len(answers)
            answers.clear()
            toRemove.clear()
            firstPeople = True
            
        else :
            if firstPeople :
                for c in line.rstrip():
                    answers.add(c)
                
            else :
                for key in answers:
                    if key not in line.rstrip():
                        toRemove.append(key)
                for answer in toRemove:        
                    answers.discard(answer)
                
            firstPeople = False
        
    total += len(answers)
    answers.clear()
    print("Result: ", total)

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))


