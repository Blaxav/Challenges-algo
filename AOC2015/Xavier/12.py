import json
import sys


def DFS(json_data, numbers):
    if type(json_data) is dict:
        if "red" not in json_data.values():
            for key in json_data:
                # print(json_data[key])
                DFS(json_data[key], numbers)
    elif type(json_data) is list:
        for v in json_data:
            DFS(v, numbers)
    elif type(json_data) is int:
        numbers.append(json_data)
        # print(numbers)


if __name__ == '__main__':

    input_data = open(sys.argv[1], 'r')
    data = input_data.readline()
    input_data.close()

    input_data = open(sys.argv[1], 'r')
    json_data = json.load(input_data)
    input_data.close()

    numbers = []
    c_int = "0"
    for e in data:
        # print(e, "  ", e.isnumeric())
        if e.isnumeric():
            c_int += e
        else:
            if c_int not in ["0", "-"]:
                numbers.append(int(c_int))
            if e == '-':
                c_int = "-"
            else:
                c_int = "0"

    # print(numbers)
    print("Result : ", sum(numbers))

    numbers = []
    DFS(json_data, numbers)
    print(sum(numbers))
