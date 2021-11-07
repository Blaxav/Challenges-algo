import hashlib
import sys


def md5_begin(message, int, sizeOfReturn):
    return hashlib.md5((message + str(int)).encode()).hexdigest()[:sizeOfReturn]


if __name__ == "__main__":
    message = sys.argv[1]
    code = 0
    while md5_begin(message, code, 5) != "00000":
        code += 1
    print("The code is ", code)

    code = 0
    while md5_begin(message, code, 6) != "000000":
        code += 1
    print("The code is ", code)
