from time import time
from collections import deque
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

            
def part1(scheme: list):
    mask, memory = '', dict()
    for elem in scheme:
        if elem.startswith('mask'):
            mask = elem[7:]
        else:
            adress, value = elem.replace('mem[', '').split('] = ')
            stringValue = str(bin(int(value)))[2:]
            stringValue36bytes = '0' * (36-len(stringValue)) + stringValue
            newValue = ''
            for it in range(36):
                if mask[it] == 'X':
                    newValue += stringValue36bytes[it]
                else:
                    newValue += mask[it]
            memory[adress] = int(newValue, 2)
    
    return sum(memory.values())

def part2(scheme: list):
    mask, memory = '', dict()
    for elem in scheme:
        if elem.startswith('mask'):
            mask = elem[7:]
        else:
            adress, value = elem.replace('mem[', '').split('] = ')
            stringAdress = str(bin(int(adress)))[2:]
            stringAdress36bytes = '0' * (36-len(stringAdress)) + stringAdress
            newAdress = ''
            for it in range(36):
                if mask[it] == '0':
                    newAdress += stringAdress36bytes[it]
                else:
                    newAdress += mask[it]
            adressesWithX, adressesWithoutX = deque([newAdress]), list()
            while adressesWithX:
                currentAdress = adressesWithX.popleft()
                if 'X' not in currentAdress:
                    adressesWithoutX.append(currentAdress)
                else:
                    adressesWithX.append(currentAdress.replace('X', '0', 1))
                    adressesWithX.append(currentAdress.replace('X', '1', 1))

            for adress in adressesWithoutX:
                memory[int(adress,2)] = int(value)
    
    return sum(memory.values())

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

