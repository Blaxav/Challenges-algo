from time import time
import unittest
from collections import defaultdict, deque
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def is_num(s: str):
    try:
        int(s)
    except:
        return False
    return True

def getval(regs: dict, x: str):
    if is_num(x):
        return int(x)
    else:
        return regs[x]
            
def part1(scheme: list):
    registers, it = defaultdict(int), 0
    while it in range(len(scheme)):
        instruction = scheme[it].split()
        if instruction[0] == 'snd':
            last_played_sound = getval(registers, instruction[1])
            it += 1
        elif instruction[0] == 'set':
            registers[instruction[1]] = getval(registers, instruction[2])
            it += 1
        elif instruction[0] == 'add':
            registers[instruction[1]] += getval(registers, instruction[2])
            it += 1
        elif instruction[0] == 'mul':
            registers[instruction[1]] *= getval(registers, instruction[2])
            it += 1
        elif instruction[0] == 'mod':
            registers[instruction[1]] %= getval(registers, instruction[2])
            it += 1
        elif instruction[0] == 'rcv':
            if getval(registers, instruction[1]) != 0:
                return last_played_sound
        elif instruction[0] == 'jgz':
            if getval(registers, instruction[1]) != 0:
                it += getval(registers, instruction[2])
            else:
                it += 1

def part2(scheme: list):
    registers = {0: defaultdict(int), 1: defaultdict(int)}
    registers[0]['p'] = 0
    registers[1]['p'] = 1
    it = [0, 0]
    queues = [deque([]), deque([])]
    sent_values = [0, 0]
    is_program_waiting = [False, False]
    current_running_program = 0
    other_program = 1
    while True:
        instruction = scheme[it[current_running_program]].split()
        if instruction[0] == 'snd':
            queues[current_running_program].append(getval(registers[current_running_program], instruction[1]))
            it[current_running_program] += 1
            sent_values[current_running_program] += 1
            if is_program_waiting[other_program]:
                is_program_waiting[other_program] = False
        elif instruction[0] == 'set':
            registers[current_running_program][instruction[1]] = getval(registers[current_running_program], instruction[2])
            it[current_running_program] += 1
        elif instruction[0] == 'add':
            registers[current_running_program][instruction[1]] += getval(registers[current_running_program], instruction[2])
            it[current_running_program] += 1
        elif instruction[0] == 'mul':
            registers[current_running_program][instruction[1]] *= getval(registers[current_running_program], instruction[2])
            it[current_running_program] += 1
        elif instruction[0] == 'mod':
            registers[current_running_program][instruction[1]] %= getval(registers[current_running_program], instruction[2])
            it[current_running_program] += 1
        elif instruction[0] == 'jgz':
            if getval(registers[current_running_program], instruction[1]) > 0:
                it[current_running_program] += getval(registers[current_running_program], instruction[2])
            else:
                it[current_running_program] += 1
        elif instruction[0] == 'rcv':
            if len(queues[other_program]) != 0:
                registers[current_running_program][instruction[1]] = queues[other_program].popleft()
                it[current_running_program] += 1
            else:
                is_program_waiting[current_running_program] = True
                if is_program_waiting[other_program]:
                    return sent_values[1]
                else:
                    current_running_program, other_program = other_program, current_running_program


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

