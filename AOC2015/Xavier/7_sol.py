from ctypes import c_ushort

lines = []
with open('input_day7.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

sig = {}
gates = {}


def perform(inst):
    ##print("** Performing: " + inst)
    global sig
    global gates
    if inst.isdigit():
        #print("!!Found digit!!")
        # if y == 'a': #print("a <- {}".format(c_ushort(int(x))))
        return c_ushort(int(inst))
    if inst.startswith("NOT"):
        operand = inst.split()[1]
        if operand in sig:
            operand = sig[operand]
        else:
            operand = findvalue(operand)
        #print("§§ Solved: " + inst)
        return c_ushort(~operand.value)
    if len(inst.split()) == 1:
        return findvalue(inst)

    #print("// Splitting: " + inst)
    a, op, b = inst.split()
    if a in sig:
        a = sig[a]
    elif a.isdigit():
        a = c_ushort(int(a))
    else:
        a = findvalue(a)

    if b in sig:
        b = sig[b]
    elif b.isdigit():
        b = c_ushort(int(b))
    else:
        b = findvalue(b)

    if op == 'AND':
        #print("§§ Solved: " + inst)
        return c_ushort(a.value & b.value)
    if op == 'OR':
        #print("§§ Solved: " + inst)
        return c_ushort(a.value | b.value)
    if op == 'LSHIFT':
        #print("§§ Solved: " + inst)
        return c_ushort(a.value << b.value)
    if op == 'RSHIFT':
        #print("§§ Solved: " + inst)
        return c_ushort(a.value >> b.value)


def findvalue(wire):
    global sig
    global gates
    #print("++ Searching for: " + wire)
    #print("++ Gate: " + gates[wire])
    # print("---")
    # print(sig)
    # print("---")
    if wire in sig:
        return wire
    else:
        gate = gates[wire]
        goal = perform(gate)
        sig[wire] = goal
        return goal


for line in lines:
    x, y = line.split(" -> ")
    gates[y] = x

# print(gates['h'])
value_a = findvalue('a').value
print("value a: {}".format(value_a))
sig = {}
sig['b'] = c_ushort(value_a)
value_a2 = findvalue('a').value
print("value a (2nd iteration): {}".format(value_a2))
