from time import time
from collections import deque
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

class Circuit:
    def __init__(self, scheme):
        self.values = dict()
        self.instructions = dict()
        self.getInstructions(scheme)
    
    def getInstructions(self, scheme):
        self.instructions = dict()
        for instruction in scheme:
            fracInstruction = instruction.split(' -> ')
            if 'AND' in fracInstruction[0]:
                wires = fracInstruction[0].split(' AND ')
                self.instructions[fracInstruction[1]] = {'operator': 'AND', 'wires': wires}
                if wires[0].isdigit():
                    self.values[wires[0]] = int(wires[0])
            elif 'OR' in fracInstruction[0]:
                wires = fracInstruction[0].split(' OR ')
                self.instructions[fracInstruction[1]] = {'operator': 'OR', 'wires': wires}
            elif 'LSHIFT' in fracInstruction[0]:
                wires = fracInstruction[0].split(' LSHIFT ')
                self.instructions[fracInstruction[1]] = {'operator': 'LSHIFT', 'wires': wires}
                if wires[1].isdigit():
                    self.values[wires[1]] = int(wires[1]) 
            elif 'RSHIFT' in fracInstruction[0]:
                wires = fracInstruction[0].split(' RSHIFT ')
                self.instructions[fracInstruction[1]] = {'operator': 'RSHIFT', 'wires': wires}
                if wires[1].isdigit():
                    self.values[wires[1]] = int(wires[1]) 
            elif 'NOT' in fracInstruction[0]:
                self.instructions[fracInstruction[1]] = {'operator': 'NOT', 'wires': [fracInstruction[0][4:]]}
            else:
                self.instructions[fracInstruction[1]] = {'operator': 'assign', 'wires': [fracInstruction[0]]}
                if fracInstruction[0].isdigit():
                    self.values[fracInstruction[0]] = int(fracInstruction[0])
    
    def gettableWires(self):
        gettableWire = []
        for k, v in self.instructions.items():
            if v['wires'] == [a for a in v['wires'] if a in self.values] and k not in self.values:
                 gettableWire.append(k)
        return gettableWire
    
    def evoluteCircuit(self):
        gettableWires = self.gettableWires()
        while gettableWires:
            for wire in gettableWires:
                operator, wires = self.instructions[wire]['operator'], self.instructions[wire]['wires']
                if operator == 'AND':
                    self.values[wire] = self.values[wires[0]] & self.values[wires[1]]
                elif operator == 'OR':
                    self.values[wire] = self.values[wires[0]] | self.values[wires[1]]
                elif operator == 'LSHIFT':
                    self.values[wire] = self.values[wires[0]] << self.values[wires[1]]
                elif operator == 'RSHIFT':
                    self.values[wire] = self.values[wires[0]] >> self.values[wires[1]] 
                elif operator == 'NOT':
                    self.values[wire] = ~self.values[wires[0]]
                elif operator == 'assign':
                    self.values[wire] = self.values[wires[0]]
            gettableWires = self.gettableWires()           
    
def part1(scheme: list):
    circuit = Circuit(scheme)
    circuit.evoluteCircuit()
    return circuit.values['a']

def part2(scheme: list):
    newB = part1(scheme)
    circuit = Circuit(scheme)
    circuit.instructions['b']['wires'][0] = str(newB)
    circuit.values[str(newB)] = newB
    circuit.evoluteCircuit()
    return circuit.values['a']

class Tests(unittest.TestCase):

    def testInstructions(self):
        instructions = ['123 -> x','456 -> y','x AND y -> d','x OR y -> e','x LSHIFT 2 -> f','y RSHIFT 2 -> g','NOT x -> h','NOT y -> i','3 AND x -> j']
        circuit = Circuit(instructions)
        expectedInstructions = {'x': {'operator': 'assign', 'wires': ['123']}, 'y': {'operator': 'assign', 'wires': ['456']}, 'd': {'operator': 'AND', 'wires': ['x', 'y']}, 'e': {'operator': 'OR', 'wires': ['x', 'y']}, 'f': {'operator': 'LSHIFT', 'wires': ['x', '2']}, 'g': {'operator': 'RSHIFT', 'wires': ['y', '2']}, 'h': {'operator': 'NOT', 'wires': ['x']}, 'i': {'operator': 'NOT', 'wires': ['y']},'j': {'operator': 'AND', 'wires': ['3', 'x']}}
        self.assertDictEqual(circuit.instructions, expectedInstructions)
        expectedValues = {'123': 123, '456': 456, '2': 2, '3': 3}
        self.assertDictEqual(circuit.values, expectedValues)
        expectedGettableWires = ['x', 'y']
        self.assertEqual(circuit.gettableWires(), expectedGettableWires)
        expectedCircuit = {'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456, 'j': 3}
        circuit.evoluteCircuit()


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

