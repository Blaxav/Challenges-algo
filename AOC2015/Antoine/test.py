import re
from random import sample

replacements = {}
with open('19-input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[:-2]:
        line = line.strip().split(' => ')
        replacements[line[1]]= line[0]
    inp = lines[-1].strip()

pattern = re.compile('|'.join(replacements))


steps = 0
final = inp
while final != 'e':
    temp = final
    for n in sample(list(replacements), len(replacements)):
        if n in final:
            steps += final.count(n)
            final = final.replace(n, replacements[n])
    if final == temp:
        print('ok')
        final = inp
        steps = 0
        continue

print(steps)