from sys import argv
from time import time

if __name__ == '__main__':

    if len(argv) < 2:
        print("Usage : python3 6.py file_path")
        print("   ex : python3 6.py input/6.txt")
        exit()
    N_steps = 256

    input_data = open(argv[1], 'r')
    all_fishes = [int(i)
                  for i in input_data.readline().rstrip('\n').split(',')]
    input_data.close()

    # There are 7 groups of fish
    n_groups = 7
    fishes = [0]*n_groups
    for f in all_fishes:
        fishes[f] += 1
    # new fishes are new born fishes
    new_fishes = 0
    # Waiting fishes will enter the cycle next iteration and sum up with a fish group
    waiting_fishes = 0

    t0 = time()
    id = 0
    for t in range(N_steps):
        temp = waiting_fishes

        waiting_fishes = new_fishes
        new_fishes = fishes[id]
        fishes[id] += temp

        if t == 79:
            print("After 80  days, total = ", sum(
                fishes) + new_fishes + waiting_fishes)
        id = (id + 1) % n_groups

    print("After", N_steps, "days, total = ",
          sum(fishes) + new_fishes + waiting_fishes)
    print("Time %-1.3es" % (time() - t0))
