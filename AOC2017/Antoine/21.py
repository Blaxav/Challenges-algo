from time import time
from math import sqrt
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return {i.strip().split(' => ')[0].replace('/', ''): i.strip().split(' => ')[1].replace('/', '') for i in f.readlines()}

def divide_pattern_in_squares(pattern: str) -> list:
    # Cette fonction prend en argument un carré entier et fournit une liste de carré de taille 2 ou 3
    pattern_length = int(sqrt(len(pattern)))
    if pattern_length <= 3:
        return [pattern]
    else:
        divided_pattern = []
        for divider in range(2, 4): # On essaye de diviser par 2 ou 3 uniquement
            if pattern_length % divider == 0:
                for y in range(pattern_length // divider): # On boucle sur les carrés de taille divider
                    for x in range(pattern_length // divider):
                        square = ''
                        for it in range(divider): # On créé des carrés de taille divider
                            y_position = (y * divider + it) * pattern_length
                            x_position = x * divider
                            square += pattern[y_position + x_position : y_position + x_position + divider]

                        divided_pattern.append(square)
        
                return divided_pattern

def linear_coord_to_yx_coord(linear_coord: int, pattern_length: int):
    return divmod(linear_coord, pattern_length)

def yx_coord_to_linear_coord(yx_coord: tuple, pattern_length):
    return yx_coord[0] * pattern_length + yx_coord[1]

def generate_one_rotation(square: str):
    square_length = int(sqrt(len(square)))
    center_offset = (square_length - 1) / 2
    rotated_square = ''
    for it in range(square_length ** 2):
        yx_coord = linear_coord_to_yx_coord(it, square_length)
        translated_yx_coord = (yx_coord[0] - center_offset, yx_coord[1] - center_offset)
        translated_rotated_yx_coord = (translated_yx_coord[1], -translated_yx_coord[0])
        rotated_yx_coord = (translated_rotated_yx_coord[0] + center_offset, translated_rotated_yx_coord[1] + center_offset)
        rotated_linear_coord = int(yx_coord_to_linear_coord(rotated_yx_coord, square_length))
        rotated_square += square[rotated_linear_coord]
    
    return rotated_square

def generate_flip(square: str):
    square_length = int(sqrt(len(square)))
    flipped_square = ''
    for it in range(square_length ** 2):
        yx_coord = linear_coord_to_yx_coord(it, square_length)
        flipped_yx_coord = (yx_coord[0], square_length - 1 - yx_coord[1])
        flipped_linear_coord = yx_coord_to_linear_coord(flipped_yx_coord, square_length)
        flipped_square += square[flipped_linear_coord]
    
    return flipped_square

def generate_rotations(square: str):
    rotations = []
    flipped_square = generate_flip(square)
    for it in range(4):
        square = generate_one_rotation(square)
        flipped_square = generate_one_rotation(flipped_square)
        rotations.append(square)
        rotations.append(flipped_square)
    
    return rotations

def merge_squares_in_pattern(new_pattern: list):
    new_string_pattern = ''
    new_pattern_elements_amount = sum(len(square) for square in new_pattern)
    new_pattern_length = int(sqrt(new_pattern_elements_amount))
    inside_square_length = int(sqrt(len(new_pattern[0])))
    squares_amount_on_one_line = new_pattern_length // inside_square_length
    for it in range(new_pattern_elements_amount):
        y_coord, x_coord = linear_coord_to_yx_coord(it, new_pattern_length)
        y_square_coord, x_square_coord = y_coord // inside_square_length, x_coord // inside_square_length
        square_id = y_square_coord * squares_amount_on_one_line + x_square_coord
        y_inside_square, x_inside_square = y_coord - y_square_coord * inside_square_length, x_coord - x_square_coord * inside_square_length
        elem_id = y_inside_square * inside_square_length + x_inside_square
        new_string_pattern += new_pattern[square_id][elem_id]
    
    return new_string_pattern


def part1(scheme: list, starting_pattern: str):
    new_string_pattern = starting_pattern
    for it in range(18):
        print(it)
        new_pattern = []
        divided_pattern = divide_pattern_in_squares(new_string_pattern)
        for square in divided_pattern:
            rotations = generate_rotations(square)
            for rotation in rotations:
                if rotation in scheme:
                    new_pattern.append(scheme[rotation])
                    break
        new_string_pattern = merge_squares_in_pattern(new_pattern)
            
    return new_string_pattern.count('#')

def part2(scheme: list):
    return 0

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(divide_pattern_in_squares('.#...####'), ['.#...####'])
        self.assertEqual(divide_pattern_in_squares('#..#........#..#'), ['#...', '.#..', '..#.', '...#'])
        self.assertEqual(divide_pattern_in_squares('##.##.#..#........##.##.#..#........'), ['###.', '.#.#', '#...', '..##', '...#', '..#.', '#...', '.#..', '....'])
        self.assertEqual(divide_pattern_in_squares('#.#...#....#####.#...##...##.#...#....#####.#...##...##.#...#....#####.#...##...#'),
        ['#.#..#...', '...#####.', '#..#.#..#', '#.#..#...', '...#####.', '#..#.#..#', '#.#..#...', '...#####.', '#..#.#..#'])
        self.assertEqual(generate_one_rotation('.#...####'), '.###.#..#')
        self.assertEqual(generate_one_rotation('##.#.......##.#.'), '#.#....##...#..#')
        self.assertEqual(generate_flip('.#...####'), '.#.#..###')
        self.assertEqual(generate_flip('##.#.......##.#.'), '#.##....#....#.#')
        self.assertEqual(merge_squares_in_pattern(['#.##', '..#.', '.#.#', '.#..']), '#...###..#.#.#..')

if __name__ == "__main__":
    # unittest.main()
    starting_pattern = '.#...####'
    scheme = readFile()
    p1 = part1(scheme, starting_pattern)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

