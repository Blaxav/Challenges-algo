from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip().replace('{', '[').replace('}', ']')

def delete_garbages(scheme: str):
    new_scheme, is_inside_garbage, current_garbage, previous_elem_is_exclamation_character = scheme[:], False, '', False
    for elem in scheme:
        if previous_elem_is_exclamation_character and is_inside_garbage:
            previous_elem_is_exclamation_character = False
            current_garbage += elem
        elif elem == '!' and is_inside_garbage:
            previous_elem_is_exclamation_character = True
            current_garbage += elem
        elif elem == '<' and not is_inside_garbage:
            is_inside_garbage = True
            current_garbage += elem
        elif elem == '>' and is_inside_garbage:
            current_garbage += elem
            new_scheme = new_scheme.replace(current_garbage, '', 1)
            is_inside_garbage, current_garbage = False, ''
        elif is_inside_garbage:
            current_garbage += elem
    
    return new_scheme

def calculate_score(scheme: str):
    score, depth = 0, 0
    scheme_without_useless_commas = scheme.replace('[,', '[').replace(',]', ']')
    # print(scheme_without_useless_commas)
    for count, elem in enumerate(scheme_without_useless_commas):
        if elem == "[":
            depth += 1
        elif elem == "]":
            score += depth
            # if count == len(scheme_without_useless_commas) - 1 or scheme_without_useless_commas[count + 1] == ']':
            depth -= 1            
        
    return score
            
def part1(scheme: str):
    return calculate_score(delete_garbages(scheme))

def part2(scheme: str):
    garbage_amount, is_inside_garbage, current_garbage, previous_elem_is_exclamation_character = 0, False, '', False
    for elem in scheme:
        if previous_elem_is_exclamation_character and is_inside_garbage:
            previous_elem_is_exclamation_character = False
        elif elem == '!' and is_inside_garbage:
            previous_elem_is_exclamation_character = True
        elif elem == '<' and not is_inside_garbage:
            is_inside_garbage = True
        elif elem == '>' and is_inside_garbage:
            garbage_amount += len(current_garbage)
            is_inside_garbage, current_garbage = False, ''
        elif is_inside_garbage:
            current_garbage += elem
    
    return garbage_amount


class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(delete_garbages("[]"), "[]")
        self.assertEqual(delete_garbages("[[[]]]"), "[[[]]]")
        self.assertEqual(delete_garbages("[[[],[],[[]]]]"), "[[[],[],[[]]]]")
        self.assertEqual(delete_garbages("[<[],[],[[]]>]"), "[]")
        self.assertEqual(delete_garbages("[<a>,<a>,<a>,<a>]"), "[,,,]")
        self.assertEqual(delete_garbages("[[<a>],[<a>],[<a>],[<a>]]"), "[[],[],[],[]]")
        self.assertEqual(delete_garbages("[[<!>],[<!>],[<!>],[<a>]]"), "[[]]")
        self.assertEqual(part1("[]"), 1)
        self.assertEqual(part1("[[[]]]"), 6)
        self.assertEqual(part1("[[],[]]"), 5)
        self.assertEqual(part1("[[[],[],[[]]]]"), 16)
        self.assertEqual(part1("[<a>,<a>,<a>,<a>]"), 1)
        self.assertEqual(part1("[[<ab>],[<ab>],[<ab>],[<ab>]]"), 9)
        self.assertEqual(part1("[[<!!>],[<!!>],[<!!>],[<!!>]]"), 9)
        self.assertEqual(part1("[[<a!>],[<a!>],[<a!>],[<ab>]]"), 3)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

