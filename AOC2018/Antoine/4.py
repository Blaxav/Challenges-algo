from time import time
import unittest
from datetime import datetime
import re
from operator import itemgetter
from collections import defaultdict, Counter
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().replace('[', '').split('] ') for i in f.readlines()]

def adapt_scheme(scheme: list): #YYYY-MM-DD HH-MM
    for elem in scheme:
        elem[0] = datetime.strptime(elem[0], '%Y-%m-%d %H:%M')
        if "Guard" in elem[1]:
            elem[1] = re.findall(r'\d+', elem[1])[0]
    scheme = sorted(scheme, key=itemgetter(0))

    return scheme

def get_sleep_time(timetable: list):
    sleep_time_dict = defaultdict(list)
    for event in timetable:
        if event[1].isdigit():
            current_guard = int(event[1])
        elif 'asleep' in event[1]:
            sleep_time = event[0]
        else:
            wake_time = event[0]
            sleep_time_dict[current_guard] += list(range(sleep_time.minute, wake_time.minute))

    return sleep_time_dict

            
def part1(scheme: list):
    sleep_time = get_sleep_time(scheme)
    max_key = max(sleep_time, key= lambda x: len(sleep_time[x]))
    most_slept_minute = max(sleep_time[max_key], key=sleep_time[max_key].count)

    return max_key * most_slept_minute

def part2(scheme: list):
    sleep_time = get_sleep_time(scheme)
    slept_minute_counter = {k:(max(Counter(v), key=Counter(v).get), max(Counter(v).values())) for k, v in sleep_time.items()}
    max_val = max(slept_minute_counter.values(), key= lambda x: x[1])
    max_key = max_key = next(k for k, v in slept_minute_counter.items() if v == max_val)

    return max_key * slept_minute_counter[max_key][0]

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    adapted_scheme = adapt_scheme(scheme)
    p1 = part1(adapted_scheme)
    print(f"Part 1: {p1}")
    p2 = part2(adapted_scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

