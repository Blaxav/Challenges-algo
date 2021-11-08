import sys
from collections import deque, defaultdict


class IntCode(object):
    """ IntCode virtual machine """
    grid = defaultdict(str)

    def __init__(self, name, code, inp="X"):
        self.name = name
        self.program_param = {}
        self.pos = 0
        self.output = 0
        self.program = {}
        self.io = deque()
        self.manualio = deque()
        if inp != "X":
            self.manualio.append(inp)
        self.last_output = ''
        self.relative_base = 0
        self.x = 50
        self.y = 50
        self.__direction = '^'

        i = 0
        for instr in code:
            self.program[i] = instr
            i += 1

    def __str__(self):
        return 1

    def get_input(self):
        """
        Gets input for the IntCode VM
        :param self.cur_proc: Which processor is now running
        (to enable multiple codes running at the same time)
        :return: the value of input
        """

        if len(self.manualio) > 0:
            instr = self.manualio.popleft()
            print(chr(instr), end='')
            # if instr == 10:
            #    input("Press enter")
            return instr
        else:
            if len(self.io) == 0:
                inp = input("Input?:")
                inputs = list(map(ord, inp+'\n'))

                for i in inputs:
                    self.io.append(i)

            instr = self.io.popleft()

        self.last_output = ''
        return instr

    def process_output(self):
        # if we have seen all address,
        # x, y, return it and delete from the queue
        what = self.io.popleft()
        print(chr(int(what)), end='')
        self.last_output += chr(int(what))
        return 1

    def run_intcode(self):
        params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}

        while 1:
            instr = self.program[self.pos]

            op = instr % 100

            mode1 = int(instr / 100) % 10
            mode2 = int(instr / 1000) % 10
            mode3 = int(instr / 10000) % 10

            reg1 = self.program.get(self.pos + 1, 0)
            reg2 = self.program.get(self.pos + 2, 0)
            reg3 = self.program.get(self.pos + 3, 0)

            v1 = reg1

            if op != 3:
                if mode1 == 0:
                    v1 = self.program.get(reg1, 0)
                if mode1 == 2:
                    v1 = self.program.get(
                            reg1 + self.relative_base, 0)
            else:
                if mode1 == 2:
                    v1 += self.relative_base

            v2 = reg2
            if mode2 == 0:
                v2 = self.program.get(reg2, 0)
            if mode2 == 2:
                v2 = self.program.get(
                        reg2 + self.relative_base, 0)

            v3 = reg3
            if mode3 == 2:
                v3 += self.relative_base

            if op == 1:
                self.program[v3] = v1 + v2

            # Process the opcodes
            elif op == 2:
                self.program[v3] = v1 * v2

            elif op == 3:
                self.program[v1] = self.get_input()

            elif op == 4:
                self.io.append(v1)
                self.process_output()

            elif (op == 5):
                if v1 > 0:
                    self.pos = v2
                    continue

            elif op == 6:
                if v1 == 0:
                    self.pos = v2
                    continue

            elif op == 7:
                if int(v1) < int(v2):
                    self.program[v3] = 1
                else:
                    self.program[v3] = 0

            elif op == 8:
                if v1 == v2:
                    self.program[v3] = 1
                else:
                    self.program[v3] = 0

            elif op == 9:
                self.relative_base += v1

            elif op == 99:
                return self.io

            else:
                sys.exit("Unknown argument found")

            shift = params[op] + 1
            self.pos = self.pos + shift