from time import time
from itertools import permutations
import unittest
a = time()


def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]


def swap_position(message: str, position_one: int, position_two: int):
    min_position, max_position = min(position_one, position_two), max(position_one, position_two)
    return message[:min_position] + message[max_position] + message[min_position + 1:max_position] + message[min_position] + message[max_position + 1:]


def swap_letter(message: str, letter_one: str, letter_two: str):
    return swap_position(message, message.index(letter_one), message.index(letter_two))

def rotate_direction(message: str, direction: str, moves: int):
    if moves > len(message):
        moves -= len(message)
    if direction == "right":
        return message[-moves:] + message[:-moves]
    else:
        return rotate_direction(message, "right", -moves)

def rotate_position(message: str, position: int):
    return rotate_direction(message, "right", position + (1 if position < 4 else 2))

def reverse_position(message: str, position_one: int, position_two: int):
    return message[:position_one] + message[position_one:position_two + 1][::-1] + message[position_two + 1:]

def move_position(message: str, position_one: int, position_two: int):
    if position_one < position_two:
        return message[:position_one] + message[position_one + 1:position_two + 1] + message[position_one] + message[position_two + 1:]
    else:
        return message[:position_two] + message[position_one] + message[position_two:position_one] + message[position_one + 1:]


def part1(scheme: list, message: str):
    for instruction in scheme:
        split_instruction = instruction.split(' ')
        if instruction.startswith('swap position'):
            message = swap_position(message, int(split_instruction[2]), int(split_instruction[5]))
        elif instruction.startswith('swap letter'):
            message = swap_letter(message, split_instruction[2], split_instruction[5])
        elif instruction.startswith('rotate'):
            if split_instruction[1] in ['left', 'right']:
                message = rotate_direction(message, split_instruction[1], int(split_instruction[2]))
            else:
                message = rotate_position(message, message.index(split_instruction[6]))
        elif instruction.startswith('reverse'):
            message = reverse_position(message, int(split_instruction[2]), int(split_instruction[4]))
        else:
            message = move_position(message, int(split_instruction[2]), int(split_instruction[5]))
    
    return message


def part2(scheme: list, message: str):
    for elem in permutations(message):
        if part1(scheme, ''.join(elem)) == message:
            return ''.join(elem)


class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(swap_position("abcde", 4, 0), "ebcda")
        self.assertEqual(swap_letter("ebcda", "d", "b"), "edcba")
        self.assertEqual(rotate_direction("abcde", "left", 1), "bcdea")
        self.assertEqual(rotate_direction("abcde", "right", 2), "deabc")
        self.assertEqual(rotate_position("abdec", 1), "ecabd")
        self.assertEqual(rotate_position("ecabd", 4), "decab")
        self.assertEqual(reverse_position("edcba", 1, 3), "ebcda")
        self.assertEqual(reverse_position("edcba", 0, 4), "abcde")
        self.assertEqual(move_position("bcdea", 1, 4), "bdeac")
        self.assertEqual(move_position("bdeac", 3, 0), "abdec")
        self.assertEqual(part1(["swap position 4 with position 0", "swap letter d with letter b", "reverse positions 0 through 4", "rotate left 1 step", "move position 1 to position 4", "move position 3 to position 0", "rotate based on position of letter b", "rotate based on position of letter d"], "abcde"), "decab")


if __name__ == "__main__":
    # unittest.main()
    message_p1 = "abcdefgh"
    scheme = readFile()
    p1 = part1(scheme, message_p1)
    print(f"Part 1: {p1}")
    message_p2 = "fbgdceah"
    p2 = part2(scheme, message_p2)
    print(f"Part 2: {p2}")
    print(time()-a)
