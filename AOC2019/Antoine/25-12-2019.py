import sys
from intcode import IntCode
from itertools import combinations

assert len(sys.argv) == 2

code = open(sys.argv[1]).read().strip().split(',')
data = list(map(int, code))


processor = IntCode(0, data, "X")

instr_str = "east\n"+"take loom\n"+"east\n"+"take fixed point\n"+"north\n"+"take spool of cat6\n"+"north\n"+"take weather machine\n"+"south\n"+"west\n"+"take shell\n"+"east\n"+"south\n"+"west\n"+"south\n"+"take ornament\n"+"west\n"+"north\n"+"take candy cane\n"+"south\n"+"east\n"+"north\n"+"west\n"+"north\n"+"take wreath\n"+"north\n"+"east\n"
# all combinations of equipment

inventory = ['wreath', 'loom', 'fixed point', 'spool of cat6', 'shell', 'ornament', 'candy cane', 'weather machine']

for i in range(len(inventory)+1):
    for comb in combinations(inventory, i):
        # drop everything
        for inv in inventory:
            instr_str += "drop "+inv+"\n"
        for item in comb:
            instr_str += "take "+item+"\n"
        instr_str += "south\n"


instr = (list(map(ord, instr_str)))

# combin

for i in instr:
    processor.manualio.append(i)


while 1:
    processor.run_intcode()