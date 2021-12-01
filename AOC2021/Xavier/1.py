from sys import argv

if __name__ == '__main__':

    depth = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        depth.append(int(line.rstrip('\n')))
    input_data.close()

    previous_depth = depth[0]
    increase_cnt = 0
    for c_depth in depth[1:]:
        increase_cnt += int(c_depth > previous_depth)
        previous_depth = c_depth
    print('Part 1 : ', increase_cnt)

    depth_slide = [sum(depth[j:j+3]) for j in range(len(depth) - 2)]

    previous_depth = depth_slide[0]
    increase_cnt = 0
    for c_depth in depth_slide[1:]:
        increase_cnt += int(c_depth > previous_depth)
        previous_depth = c_depth
    print('Part 2 : ', increase_cnt)
