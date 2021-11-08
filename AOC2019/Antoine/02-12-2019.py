class InvalidOpcode(Exception):
    pass

class mylist(list):
    def __getitem__(self, item):
        try:
            return super(mylist,self).__getitem__(item)
        except IndexError as e:
            if item < 0: raise IndexError()
            super(mylist,self).extend([0]*(item + 1 - super(mylist,self).__len__()))
            return super(mylist,self).__getitem__(item)

    def __setitem__(self, idx, val):
        try:
            return super(mylist,self).__setitem__(idx,val)
        except IndexError as e:
            if idx < 0: raise IndexError()
            super(mylist,self).extend([0]*(idx + 1 - super(mylist,self).__len__()))
            return super(mylist,self).__setitem__(idx,val)

def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def getOutput(vals : list):
    vals = mylist(vals)
    i = 0
    while 1:
        opcode = vals[i]

        # 0 Parameter
        if opcode in [99]: # Termination
            return vals
        
        # 3 Parameter
        elif opcode in [1,2]:
            a = vals[i+1]
            b = vals[i+2]
            c = vals[i+3]
            if opcode == 1: # Addition
                vals[c] = vals[a] + vals[b]
            elif opcode == 2: # Multiplication
                vals[c] = vals[a] * vals[b]
            i += 4

        else:
            raise InvalidOpcode()

def part1(vals : list):
    memory = vals.copy()
    memory[1] = 12
    memory[2] = 2
    return getOutput(memory)[0]

def part2(vals : list):
    for noun in range(100):
        for verb in range(100):
            memory = vals.copy()
            memory[1], memory[2] = noun, verb
            if getOutput(memory)[0] == 19690720:
                return noun * 100 + verb


if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")

