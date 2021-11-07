from sys import argv


def filter(input_stream):
    while True:
        try:
            id = input_stream.index("!")
            input_stream = input_stream[:id] + input_stream[id + 2:]
        except:
            return input_stream


def clear_garbage(stream):
    while True:
        try:
            garbage_beg = stream.index("<")
            garbage_end = stream.index(">")
            stream = stream[:garbage_beg] + stream[garbage_end+1:]
        except:
            return stream


def clean(stream):
    stream = filter(stream)
    stream = clear_garbage(stream)
    return stream


if __name__ == '__main__':

    # Part 1
    input_data = open(argv[1], 'r')
    stream = input_data.readline().rstrip('\n')
    input_data.close()

    stream = clean(stream)
    print(stream)
