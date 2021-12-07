from sys import argv

if __name__ == '__main__':

    N_steps = int(argv[2])

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

    id = 0
    for t in range(N_steps):
        temp = waiting_fishes

        waiting_fishes = new_fishes
        new_fishes = fishes[id]
        fishes[id] += temp

        # print("After ", t+1, " days, total = ", sum(
        #    fishes) + new_fishes + waiting_fishes)
        id = (id + 1) % n_groups

    print("After ", N_steps, " days, total = ",
          sum(fishes) + new_fishes + waiting_fishes)
