import sys


def apply(val):

    result = ""

    counter = 1
    cur_value = val[0]
    id = 1

    while id < len(val):
        if cur_value == val[id]:
            counter += 1
        else:
            result += str(counter) + val[id-1]
            counter = 1
            cur_value = val[id]

        id += 1

    result += str(counter) + val[id - 1]
    #print(val, " -> ", result)
    return result


if __name__ == '__main__':

    val = "1321131112"

    N = 50

    for k in range(N):
        val = apply(val)

    print("Result : ", len(val))
