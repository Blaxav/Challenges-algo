from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def analyze_corruption(line: str):
    match_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}
    open_chars = list()
    for elem in line:
        if elem in match_chars.keys():
            open_chars.append(elem)
        elif elem in match_chars.values():
            last_opened_char = open_chars.pop()
            if match_chars[last_opened_char] != elem:
                return True, elem
    
    return False, open_chars

def get_syntax_error_score(line: str):
    is_corrupted, corruptant_elem = analyze_corruption(line)
    corruption_score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    if is_corrupted:
        return corruption_score_table[corruptant_elem]
    else:
        return 0
            
def part1(scheme: list):
    return sum(get_syntax_error_score(line) for line in scheme)

def get_completion_score(line: str):
    is_corrupted, remaining_open_chars = analyze_corruption(line)
    match_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}
    completion_score_matching = {')': 1, ']': 2, '}': 3, '>': 4}
    if not is_corrupted:
        completion_score = 0
        completion_chars = [match_chars[opened_char] for opened_char in remaining_open_chars][::-1]
        for elem in completion_chars:
            completion_score *= 5
            completion_score += completion_score_matching[elem]

        return completion_score

def part2(scheme: list):
    completion_list_score = list()
    for line in scheme:
        completion_score = get_completion_score(line)
        if completion_score:
            completion_list_score.append(completion_score)
    sorted_completion_list_score = sorted(completion_list_score)
    
    return sorted_completion_list_score[(len(sorted_completion_list_score) - 1) // 2]

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

