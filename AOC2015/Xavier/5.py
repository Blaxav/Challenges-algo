import sys


def rule_vowels(message):
    total = 0
    for vow in ['a', 'e', 'i', 'o', 'u']:
        total += message.count(vow)
    return total


def rule_nuplet(message, n):
    i0 = 0
    cnt = 1

    for letter in message[i0+1:]:
        if letter == message[i0]:
            cnt += 1
        else:
            #print(message[i0:i0+cnt], end='')
            i0 = i0 + cnt
            cnt = 1

        if cnt == n:
            # print(message[i0:i0+cnt])
            return True
    return False


def rule_forbidden(message, list_of_strings):
    for substr in list_of_strings:
        if message.count(substr) > 0:
            return True
    return False


def rule_pair_appears_twice(message):
    for i0 in range(0, len(message) - 3):
        for j in range(i0+2, len(message) - 1):
            if message[i0:i0+2] == message[j:j+2]:
                return True
    return False


def rule_letter_repeated_with_one_sep(message):
    for i in range(0, len(message) - 2):
        if message[i] == message[i+2]:
            return True
    return False


if __name__ == '__main__':
    forbiddens = ["ab", "cd", "pq", "xy"]

    total_part1 = 0
    total_part2 = 0

    input_file = open(sys.argv[1], 'r')
    for message in input_file:
        if rule_vowels(message) >= 3 \
                and rule_nuplet(message, 2) \
                and not rule_forbidden(message, forbiddens):
            total_part1 += 1

        if rule_pair_appears_twice(message) \
                and rule_letter_repeated_with_one_sep(message):
            total_part2 += 1
    input_file.close()

    print("Number of nice strings part 1 : ", total_part1)
    print("Number of nice strings part 2 : ", total_part2)
