
from collections import deque
from sys import argv

if __name__ == '__main__':

    chunks = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        chunks.append(line.rstrip('\n'))
    input_data.close()

    opening = "({[<"
    closing = {"(": ")", "{": "}", "[": "]", "<": ">"}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    completion_values = {")": 1, "]": 2, "}": 3, ">": 4}
    completion_scores = []

    open_chars = deque()
    total_score = 0
    for chunk in chunks:
        open_chars.clear()
        corrupted = False
        for c in chunk:
            if c in opening:
                open_chars.append(c)
            else:
                c_open = open_chars.pop()
                if c != closing[c_open]:
                    total_score += scores[c]
                    corrupted = True
        # Part 2
        if not corrupted:
            compl_score = 0
            while open_chars:
                compl_score *= 5
                compl_score += completion_values[closing[open_chars.pop()]]
            completion_scores.append(compl_score)

    print("Part 1 : ", total_score)
    n_completion = len(completion_scores)
    print("Part 2 : ", sorted(completion_scores)[int((n_completion-1)/2)])
