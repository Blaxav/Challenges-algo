from collections import defaultdict, deque
from sys import argv


class Operation:
    def __init__(self, typeOp, register, value):
        self.type = typeOp
        self.register = register
        self.value = value


def run(registers, operations, state, queue, send, cid, id):

    while state[cid] == "ready":

        op = operations[id]

        if op.type == "snd":
            # Send a value to the other program and set its state to waiting, so that
            # the other program is not waiting anymore
            queue[(cid+1) % 2].append(registers[op.register])
            send[cid] += 1
            if state[(cid+1) % 2] == "waiting":
                state[(cid+1) % 2] = "ready"
            id += 1
        elif op.type == "set":
            registers[op.register] = registers[op.value]
            id += 1
        elif op.type == "add":
            registers[op.register] += registers[op.value]
            id += 1
        elif op.type == "mul":
            registers[op.register] *= registers[op.value]
            id += 1
        elif op.type == "mod":
            registers[op.register] %= registers[op.value]
            id += 1
        elif op.type == "rcv":
            if len(queue[cid]) > 0:
                registers[op.register] = queue[cid].popleft()
            else:
                state[cid] = "waiting"
                break
            id += 1
        elif op.type == "jgz":
            if registers[op.register] > 0:
                id += registers[op.value]
            else:
                id += 1
        else:
            print("invalid operation type ", op.type)
            exit()

        if id >= len(operations):
            state[cid] = "terminated"

    return id


if __name__ == '__main__':

    operations = []
    registers = dict()

    input_data = open(argv[1], 'r')
    for line in input_data:
        typeOp, reg = line.rstrip('\n').split()[:2]
        val = 0
        registers[reg] = 0
        if len(line.rstrip('\n').split()) == 3:
            val = line.rstrip('\n').split()[2]
            registers[val] = int(val) if val.lstrip('-').isdigit() else 0
        operations.append(Operation(typeOp, reg, val))
    input_data.close()

    # Part 1
    ####################
    id = 0
    sound = 0
    while id < len(operations):
        op = operations[id]

        if op.type == "snd":
            sound = registers[op.register]
            id += 1
        elif op.type == "set":
            registers[op.register] = registers[op.value]
            id += 1
        elif op.type == "add":
            registers[op.register] += registers[op.value]
            id += 1
        elif op.type == "mul":
            registers[op.register] *= registers[op.value]
            id += 1
        elif op.type == "mod":
            registers[op.register] %= registers[op.value]
            id += 1
        elif op.type == "rcv":
            if registers[op.register] != 0:
                print("Part 1 : ", sound)
                break
            id += 1
        elif op.type == "jgz":
            id += registers[op.value] if registers[op.register] > 0 else 1
        else:
            print("invalid operation type ", op.type)
            exit()

    # Part 2
    ####################
    # Initialization of both registers

    registers2 = [dict(), dict()]
    '''
    state can be : 
        - ready: ready to execute instructions
        - waiting: wainting for the other program to send a value (queue is empty)
        - terminated: has already executed all the instructions
    '''
    state = ["ready", "ready"]
    queue = [deque(), deque()]
    send = [0, 0]

    # Current running operation in each program
    opid = [0, 0]

    for i in range(2):
        for val in registers:
            registers2[i][val] = int(val) if val.lstrip('-').isdigit() else 0
        registers2[i]['p'] = i

    # Current id of running program
    cid = 0
    itCnt = 0
    while True:
        try:
            # try finding index of "ready" in state, if it fails,
            # both programs terminated
            state.index("ready")
            
            # run current program until it stops
            opid[cid] = run(registers2[cid], operations,
                            state, queue, send, cid, opid[cid])

            if cid == 1:
                break
            #print("Program ", cid, "  ", state, "  ", queue)

            # change running program
            cid = (cid + 1) % 2

            itCnt += 1
            if itCnt % 10000 == 0:
                print(itCnt, send)
        except:
            print("End of both programs !")
            break

    print("Part 2 : ", send[1])
