from sys import argv


def filter(stream):
    ''' filter deletes all the "!" characters with the directly following character'''
    while True:
        try:
            id = stream.index("!")
            stream = stream[:id] + stream[id + 2:]

        except:
            return stream


def clear_garbage(stream, garbage_counter):
    ''' clear_garbage deletes all the garbages in a stream with no "!" character'''
    while True:
        try:
            garbage_beg = stream.index("<")
            garbage_end = stream.index(">")
            garbage_counter.append(garbage_end - garbage_beg - 1)
            stream = stream[:garbage_beg] + stream[garbage_end+1:]
        except:
            return stream


def clean(stream, garbage_counter):
    stream = filter(stream)
    stream = clear_garbage(stream, garbage_counter)
    stream = stream.replace(",", "")
    return stream


def check_valid_substream(stream):
    return stream[0] == '{' and stream[-1] == '}'


def score(stream, depth):
    if not check_valid_substream(stream):
        print("ERROR : Invalid stream ", stream)
        exit()
    else:
        c_score = 1 + depth
        for group in subgroups(stream[1:-1]):
            c_score += score(group, depth + 1)
        return c_score


def subgroups(stream):
    '''
    Returns a stream as a list of the groups composing it at the upper level
    {aze},{tr{blabla}} is composed of two groups:
        {aze}
        {tr{blabla}}
    '''
    groups = []
    id = 0
    nbr_brackets_open = 0
    while id < len(stream):
        if stream[id] == '{':
            nbr_brackets_open += 1
        elif stream[id] == '}':
            nbr_brackets_open -= 1

        if nbr_brackets_open == 0:
            groups.append(stream[:id+1])
            stream = stream[id+1:]
            id = 0
        else:
            id += 1

    return groups


if __name__ == '__main__':

    # Part 1
    input_data = open(argv[1], 'r')
    stream = input_data.readline().rstrip('\n')
    input_data.close()

    # a list of the number of characters inside each garbage group
    # the result of part 2 is sum(garbage_counter)
    garbage_counter = []
    stream = clean(stream, garbage_counter)

    # The value of a group is the value of the level of the group (depth) +
    # the sum of the values of the groups inside
    # The total value is the value of the global group
    print("Part 1 : ", score(stream, 0))
    print("Part 2 : ", sum(garbage_counter))
