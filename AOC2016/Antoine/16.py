from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def dragon_curve(data: str):
    copied_data = data[::-1].replace("1", "2").replace("0", "1").replace("2", "0")

    return f"{data}0{copied_data}"

def partial_checksum(data: str):
    partial_checksum = ""
    for elem in [data[i:i+2] for i in range(len(data)-1) if i%2 == 0]:
        partial_checksum += "0" if "0" in elem and "1" in elem else "1"
    
    return partial_checksum

            
def part1(scheme: str, disk_size: int):
    expanded_scheme = scheme

    while len(expanded_scheme) < disk_size:
        expanded_scheme = dragon_curve(expanded_scheme)
    final_scheme = expanded_scheme[:disk_size]

    while len(final_scheme) % 2 == 0:
        final_scheme = partial_checksum(final_scheme)

    return final_scheme


class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(dragon_curve("1"), "100")
        self.assertEqual(dragon_curve("0"), "001")
        self.assertEqual(dragon_curve("11111"), "11111000000")
        self.assertEqual(dragon_curve("111100001010"), "1111000010100101011110000")
        self.assertEqual(partial_checksum("110010110100"), "110101")
        self.assertEqual(part1("10000", 20), "01100")


if __name__ == "__main__":
    # unittest.main()
    scheme, disk_size_p1, disk_size_p2 = readFile()
    p1 = part1(scheme, int(disk_size_p1))
    print(f"Part 1: {p1}")
    p2 = part1(scheme, int(disk_size_p2))
    print(f"Part 2: {p2}")
    print(time()-a)

