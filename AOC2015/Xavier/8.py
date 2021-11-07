import re
import sys


def process(message):
    id = 1
    len_message = 0

    #print("PROCESSING ", message)
    while id < len(message) - 1:
        len_message += 1
        if message[id] == '\\':
            # Escape one character
            if message[id+1] in ['\\', '"']:
                id += 1

            # Hexadecimal code format \x..
            elif message[id+1] == "x":
                id += 3
        #print(message[id], "  ", len_message)
        id += 1
    return len_message


def process_encoding(message):

    len_message = 0

    for c in message:

        len_message += 1
        if c in ['\\', '"']:
            len_message += 1
        #print(c, "  ", len_message)
    return len_message + 2


'''
########################################################################################
########################################################################################
'''
if __name__ == '__main__':

    total = 0
    total_part2 = 0
    stringline = ""
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        stringline = line.rstrip('\n')
        len_message = process(stringline)
        len_encoding = process_encoding(stringline)
        # print(stringline, " CODE : ", len(
        #    stringline), "  MESSAGE : ", len_message, " ENCODING : ", len_encoding)
        total += len(stringline) - len_message
        total_part2 += len_encoding - len(stringline)
    input_file.close()

    print("Result part 1 : ", total)
    print("Result part 2 : ", total_part2)
