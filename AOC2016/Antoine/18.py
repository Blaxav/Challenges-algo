from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def new_tile(string: str):
    return "^" if string in ["^^.", ".^^", "^..", "..^"] else "."
            
def part1(scheme: str, row_amount: int):
    initial_length = len(scheme)
    for it in range(row_amount-1):
        new_line = ""
        for pos in range(initial_length):
            if pos == 0:
                new_line += new_tile("." + scheme[initial_length * it:initial_length * it + 2])
            elif pos == initial_length - 1:
                new_line += new_tile(scheme[-2:] + ".")
            else:
                new_line += new_tile(scheme[initial_length * it + pos - 1:initial_length * it + pos + 2])
        scheme += new_line
    
    return scheme.count(".")


class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1(".^^.^.^^^^", 10), 38)


if __name__ == "__main__":
    # unittest.main()
    scheme, row_amount = readFile(), 40
    p1 = part1(scheme, 40)
    print(f"Part 1: {p1}")
    p2 = part1(scheme, 400000)
    print(f"Part 2: {p2}")
    print(time()-a)

