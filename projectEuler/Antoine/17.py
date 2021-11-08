from time import time
import math
import unittest
a = time()

def number_to_string(num: int):
    translation_dict = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"}

    if num < 20: 
        return translation_dict[num]
    elif num < 100:
        return translation_dict[(num // 10) * 10] + translation_dict[num % 10]
    elif num < 1000:
        hundred = num // 100
        tens = num - hundred * 100
        return translation_dict[hundred] + translation_dict[100] + ( "and" + number_to_string(tens) ) * ( num % 100 != 0 )
    else:
        return "onethousand"



class Tests(unittest.TestCase):

    def test(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    res = 0
    for it in range(1, 1001):
        res += len(number_to_string(it))
    print(f"The answer is {res}")
    print(time()-a)

