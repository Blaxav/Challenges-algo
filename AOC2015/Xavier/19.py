import re
import sys
from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=None)
def step(mol):
    min_path = 1e9
    if mol == 'e':
        return 0
    else:
        for product in all_products(reactions, mol):
            min_path = min([min_path, step(product)])
    return min_path + 1


def all_products(reactions, molecule):
    results = set()

    for r in reactions:
        regexp = re.compile(r)
        for pos in [(m.start(), m.end()) for m in regexp.finditer(molecule)]:
            for prod in reactions[r]:
                new_mol = molecule[:pos[0]] + prod + molecule[pos[1]:]
                results.add(new_mol)

    return list(results)


reactions = defaultdict(list)
molecule = ""
part1 = True

input_data = open(sys.argv[1], 'r')
for line in input_data:
    if line == "\n":
        part1 = False
    elif part1:
        reactions[line.split(" => ")[0]].append(line.split(" => ")[
            1].rstrip('\n'))
    else:
        molecule = line.rstrip('\n')

for r in reactions:
    print(r, " -> ", reactions[r])

print(molecule)
size_mol = len(molecule)

print("\nResolution")

part1 = len(all_products(reactions, molecule))
print("Part 1 : ", part1)

print()
print("Part 2")

####################################################################################
# Reverting operations

new_reactions = {}
for r in reactions:
    for prod in reactions[r]:
        new_reactions[prod] = r
reactions = new_reactions
mols = [molecule]

print("Part2: ", step(molecule))
exit()

n_step = 1e9
dico_times = defaultdict(lambda: 1e9)
dico_times[molecule] = 0
it_cnt = 0
id_mol = 0
cnt_molecules = defaultdict(int)
while mols:
    current_products = all_products(reactions, mols[-1])
    current_mol = mols[-1]
    mols = mols[:-1]

    print(current_mol)

    for product in current_products:
        cnt_molecules[product] += 1
        if "e" in product:
            if product == "e":
                n_step = min([n_step, dico_times[current_mol] + 1])
                print(len(mols), "  ", n_step, "   ", min([len(e) for e in mols] + [0]),
                      "   ",  max([len(e) for e in mols] + [0]))
        else:
            dico_times[product] = min(
                [n_step, dico_times[current_mol] + 1])
            if product not in mols:
                mols.append(product)

    it_cnt += 1
    if it_cnt % 5000 == 0:
        print(len(mols), "  ", n_step, "   ", min(
            [len(e) for e in mols] + [0]), "   ",  max([len(e) for e in mols] + [0]))

print(cnt_molecules)
print("Total : ", n_step)
exit()

####################################################################################
n_step = 1e9
dico_times = defaultdict(lambda: 1e9)

mols = ['e']
dico_times['e'] = 0

it_cnt = 0
while mols:
    current_products = all_products(reactions, mols[-1])
    current_mol = mols[-1]
    mols = mols[:-1]

    for product in current_products:
        if len(product) <= size_mol:
            if product == molecule:
                n_step = min([n_step, dico_times[current_mol] + 1])
            else:
                if product not in dico_times:
                    mols.append(product)
                dico_times[product] = min(
                    [n_step, dico_times[current_mol] + 1])

    it_cnt += 1
    if it_cnt % 5000 == 0:
        print(len(mols), "  ", n_step, "  ", len(dico_times))

print("Total : ", n_step)
