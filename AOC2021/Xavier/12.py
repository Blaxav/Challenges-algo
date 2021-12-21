from collections import defaultdict, deque
from sys import argv


class Path:
    def __init__(self, init, has_double):
        self.way = [i for i in init]
        self.has_double = has_double


if __name__ == '__main__':

    edges = []
    unique_nodes = set()
    capital_nodes = set()
    neighbors = defaultdict(set)

    input_data = open(argv[1], 'r')
    for line in input_data:
        nodeA = line.split('-')[0]
        nodeB = line.rstrip('\n').split('-')[1]
        for node in (nodeA, nodeB):
            if node[0].isupper():
                capital_nodes.add(node)
            else:
                unique_nodes.add(node)

        if nodeB != "start":
            neighbors[nodeA].add(nodeB)
        if nodeA != "start":
            neighbors[nodeB].add(nodeA)
    input_data.close()

    paths = deque([["start"]])
    total_paths = 0
    while paths:
        current_path = paths.pop()
        for n in neighbors[current_path[-1]]:
            if n == "end":
                # print(current_path + ["end"])
                total_paths += 1
            elif n in capital_nodes:
                paths.append(current_path + [n])
            else:
                if n not in current_path:
                    paths.append(current_path + [n])
    print("Part 1 : ", total_paths)

    paths = deque([Path(["start"], False)])
    total_paths = 0
    while paths:
        current_path = paths.pop()
        #print(current_path.way, type(current_path))
        for n in neighbors[current_path.way[-1]]:
            if n == "end":
                # print(current_path + ["end"])
                total_paths += 1
            elif n in capital_nodes:
                paths.append(
                    Path(current_path.way + [n], current_path.has_double))
            else:
                if not current_path.has_double and n in current_path.way:
                    paths.append(
                        Path(current_path.way + [n], True))
                elif n not in current_path.way:
                    paths.append(
                        Path(current_path.way + [n], current_path.has_double))
    print("Part 2 : ", total_paths)
