from sys import argv

if __name__ == '__main__':

    # Part 1
    input_data = open(argv[1], 'r')
    twists = [int(i)
              for i in input_data.readline().rstrip('\n').split(',')]
    input_data.close()

    N = int(argv[2])
    c_pos = 0
    skip_size = 0

    print(twists)
