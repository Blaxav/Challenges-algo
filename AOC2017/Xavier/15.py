from sys import argv


def generator(base, init, div):
    current = init
    while True:
        current = (current * base) % 2147483647
        while current % div != 0:
            current = (current * base) % 2147483647

        yield str(bin(current))[2:].zfill(16)[-16:]


if __name__ == '__main__':

    A = generator(16807, 873, 1)
    B = generator(48271, 583, 1)

    N = 40000000
    total = 0
    for k in range(N):
        total += int(next(A) == next(B))
        if k % 1e7 == 0:
            print(k, "  ", total)
    print("Part 1 : ", total)

    A = generator(16807, 873, 4)
    B = generator(48271, 583, 8)

    N = 5000000
    total = 0
    for k in range(N):
        total += int(next(A) == next(B))
        if k % 1e6 == 0:
            print(k, "  ", total)
    print("Part 2 : ", total)
