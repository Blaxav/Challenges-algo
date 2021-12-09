from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[elem.split(' ') for elem in i.strip().split(' | ')] for i in f.readlines()]

def part1(scheme: list):
    return sum(1 for elem in scheme for output in elem[1] if len(output) in [2, 3, 4, 7])

def get_c_and_e_elem(code_input: list):
    five_length_elem_occurences = {k: 0 for k in ['a', 'b', 'c', 'd', 'e', 'f', 'g']}

    for five_length_elem in code_input[3:6]: # On regarde les deux seuls éléments qui n'apparaissent qu'une fois dans 2, 3 et 5, ce sont b et e
        for character in five_length_elem:
            five_length_elem_occurences[character] += 1
    b_e_elems = [k for k, v in five_length_elem_occurences.items() if v == 1]

    for six_length_elem in code_input[6:9]: 
        for one_elem in code_input[0]: # On regarde le seul élément de 1 qui n'est pas dans 0, 6 et 9 -> c 
            if one_elem not in six_length_elem:
                c_elem = one_elem
        for b_e_elem in b_e_elems: # On regarde le seul élément entre b et e qui n'est pas dans 0, 6 et 9 -> e
            if b_e_elem not in six_length_elem:
                e_elem = b_e_elem

    return c_elem, e_elem

def get_line_sum(code_input: list, code_output: list):
    line_sum, obivous_elements = 0, {2: 1, 3: 7, 4: 4, 7: 8}
    c_elem, e_elem = get_c_and_e_elem(code_input)

    for count, elem in enumerate(code_output):
        power = 10 ** (3 - count)
        if len(elem) in obivous_elements:
            line_sum += obivous_elements[len(elem)] * power
        elif len(elem) == 5:
            if all(one_elem in elem for one_elem in code_input[0]): # Si tous les éléments du 1 sont dans l'élément -> 3
                line_sum += 3 * power
            else:
                if c_elem in elem: # Si l'élément possède la lettre qui représente le c -> 2
                    line_sum += 2 * power
                else: # Sinon -> 5
                    line_sum += 5 * power
        elif len(elem) == 6: 
            if all(one_elem in elem for one_elem in code_input[0]): # Si tous les éléments du 1 sont dans l'élément -> 0 ou 9
                if e_elem not in elem: # Si l'élément ne possède pas la lettre qui représente le e -> 9
                    line_sum += 9 * power
                else:
                    pass
            else: # Sinon, c'est le 6
                line_sum += 6 * power

    return line_sum


def part2(scheme: list):
    total_sum = 0
    for elem in scheme:
        sorted_input, sorted_output = sorted(["".join(sorted(code)) for code in elem[0]], key=lambda el: len(el)), ["".join(sorted(code)) for code in elem[1]]
        total_sum += get_line_sum(sorted_input, sorted_output)
    return total_sum

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

