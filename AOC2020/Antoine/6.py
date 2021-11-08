from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        answers = list()
        groupAnswer = ''
        for line in f.readlines():
            line = line.strip()
            if line:
                groupAnswer += line + '-'
            else:
                answers.append(groupAnswer)
                groupAnswer = ''
        answers.append(groupAnswer)
        return answers

def countSimilarities(answers: list):
    similarities = answers.pop()
    for char in similarities:
        for otherAnswer in answers:
            if char not in otherAnswer:
                similarities = similarities.replace(char, '')
    
    return similarities
            
def part1(scheme: list):
    return sum(len(set(elem.replace('-', ''))) for elem in scheme)

def part2(scheme: list):
    return sum([len(countSimilarities(elem[:-1].split('-'))) for elem in scheme])

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

