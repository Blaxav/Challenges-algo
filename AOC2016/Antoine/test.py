def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open("23-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def is_num(s):
    try:
        int(s)
    except:
        return False
    return True

def getval(regs, x):
    if is_num(x):
        return int(x)
    else:
        return regs[x]

def toggle(tline):
    sp = tline.split(" ")

    instr = sp[0]
    if instr == "inc":
        return " ".join(["dec"] + sp[1:])
    elif instr == "dec" or instr == "tgl":
        return " ".join(["inc"] + sp[1:])
    elif instr == "jnz":
        return " ".join(["cpy"] + sp[1:])
    elif instr == "cpy":
        return " ".join(["jnz"] + sp[1:])
    else:
        assert False

def run(lines, part2=False):
    pc = 0
    regs = {"a": 7, "b": 0, "c": 0, "d": 0}
    if part2:
        regs["a"] = 12

    while True:
        if pc >= len(lines):
            break
        line = lines[pc]

        # Instruction tracing to find the loop to optimize:
        #print pc, line

        a, b = line.split(" ", 1)

        if a == "cpy":
            b, c = b.split(" ")
            b = getval(regs, b)
            if c in regs:
                regs[c] = b
            else:
                print("invalid")
            pc += 1
        elif a == "inc":
            if b in regs:
                # Peephole optimize inc/dec/jnz loops

                # 4 cpy b c
                # 5 inc a          <<<< 0
                # 6 dec c          <<<< +1
                # 7 jnz c -2       <<<< +2
                # 8 dec d          <<<< +3
                # 9 jnz d -5       <<<< +4

                if pc + 3 < len(lines) and pc - 1 >= 0 and lines[pc-1].startswith("cpy ") and \
                    lines[pc+1].startswith("dec") and lines[pc+2].startswith("jnz") and \
                    lines[pc+3].startswith("dec") and lines[pc+4].startswith("jnz"):

                    incop = b

                    cpysrc, cpydest = lines[pc-1].split(" ")[1:]
                    dec1op = lines[pc+1].split(" ")[1]
                    jnz1cond, jnz1off = lines[pc+2].split(" ")[1:]
                    dec2op = lines[pc+3].split(" ")[1]
                    jnz2cond, jnz2off = lines[pc+4].split(" ")[1:]

                    if cpydest == dec1op and dec1op == jnz1cond and \
                        dec2op == jnz2cond and \
                        jnz1off == "-2" and jnz2off == "-5":
                            # inner loop:
                            # incop += cpysrc
                            # dec1op <- 0

                            # outer loop:
                            # dec2op times

                            # net result:  incop += (cpysrc * dec2op)
                            # dec1op, dec2op <- 0
                            regs[incop] += (getval(regs, cpysrc) * getval(regs, dec2op))
                            regs[dec1op] = 0
                            regs[dec2op] = 0
                            pc += 5
                            continue


                regs[b] += 1
            pc += 1
        elif a == "dec":
            if b in regs:
                regs[b] -= 1
            pc += 1
        elif a == "jnz":
            b, c = b.split(" ")
            b = getval(regs, b)
            c = getval(regs, c)
            if b != 0:
                pc = pc + int(c)
            else:
                pc += 1
        elif a == "tgl":
            xr = b
            x = getval(regs, xr)

            iidx = pc + x
            #print "tgl", x, iidx

            if iidx >= 0 and iidx < len(lines):
                tline = lines[iidx]
                lines[iidx] = toggle(tline)
                #print tline, "->", lines[iidx]
            pc += 1
        else:
            assert False

    return regs["a"]


print("part 1:", run(readFile()[:]))
print("part 2:", run(readFile()[:], part2=True))