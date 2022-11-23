from collections import defaultdict
from sys import argv


# class Registers inherit from defaultdict
class Registers(defaultdict):
    def __init__(self):
        super(Registers, self).__init__(lambda: 0)

    def apply(self, instruction):
        if instruction.is_valid(self):
            self[instruction.adress] += instruction.sign * instruction.value


class Instruction:
    def __init__(self, adress, signString, value, condition):
        self.adress = adress
        self.sign = 1 if signString == "inc" else -1
        self.value = value
        self.condition = condition

    def is_valid(self, registers):
        return (self.condition).is_valid(registers)


class Condition:
    def __init__(self, adress, operand, rhs):
        self.adress = adress
        self.operand = operand
        self.rhs = rhs

    def is_valid(self, registers):
        if self.operand == ">":
            return registers[self.adress] > self.rhs
        elif self.operand == ">=":
            return registers[self.adress] >= self.rhs
        elif self.operand == "<":
            return registers[self.adress] < self.rhs
        elif self.operand == "<=":
            return registers[self.adress] <= self.rhs
        elif self.operand == "==":
            return registers[self.adress] == self.rhs
        elif self.operand == "!=":
            return registers[self.adress] != self.rhs
        else:
            print("Invalid operand ", self.operand)
            exit()


if __name__ == '__main__':

    # dict of registers init to 0
    registers = Registers()

    # list of instructions
    instructions = []

    input_data = open(argv[1], 'r')
    for line in input_data:
        # 1. Finding condition
        adress = line.split()[-3]
        operand = line.split()[-2]
        rhs = int(line.rstrip('\n').split()[-1])
        condition = Condition(adress, operand, rhs)

        # 2. Creating instruction
        adress = line.split()[0]
        signString = line.split()[1]
        value = int(line.split()[2])
        instructions.append(Instruction(adress, signString, value, condition))

    input_data.close()

    max_val = 0
    for instr in instructions:
        registers.apply(instr)
        max_val = max([max_val] + list(registers.values()))
    print("Part 1 : ", max(registers.values()))
    print("Part 2 : ", max_val)
