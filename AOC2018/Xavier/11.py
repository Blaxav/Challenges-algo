from math import sqrt
from sys import argv
from time import time


class Node:
    def __init__(self, x, y, dist, father):
        self.x = x
        self.y = y
        # value of current best path to this point
        self.dist = dist
        # father node in the current path
        self.father = father
        self.heuristic_value = 1e4
        self.closed = False
        self.open = False

    def heuristic(self, target_node):
        self.heuristic_value = self.dist + \
            ((self.x - target_node.x)**2 + (self.y - target_node.y)**2)

    def update_path(self, node, final_node):
        if self.dist > node.dist:
            self.father = node.father
            self.dist = node.dist
        self.heuristic(final_node)

    def neighbors(self):
        yield(Node(self.x,      self.y + 2,   self.dist + 1, self))
        yield(Node(self.x,      self.y - 2,   self.dist + 1, self))
        yield(Node(self.x + 1,  self.y + 1,   self.dist + 1, self))
        yield(Node(self.x + 1,  self.y - 1,   self.dist + 1, self))
        yield(Node(self.x - 1,  self.y + 1,   self.dist + 1, self))
        yield(Node(self.x - 1,  self.y - 1,   self.dist + 1, self))

    def is_valid(self, final_node):
        '''
        The search is restricted to the positive quadrant 
        '''
        return self.x >= 0 and self.y >= 0 and self.x <= abs(final_node.x) and self.y <= abs(final_node.y)

    def __contains__(self, node):
        return self.x == abs(node.x) and self.y == abs(node.y)

    def __eq__(self, node):
        return self.x == abs(node.x) and self.y == abs(node.y)


def compute_final_node(path):
    '''
    Starting from origin (0, 0), following the path to compute
    the coordinates of the finale node
    path : a list of moves
    '''
    max_x = 0
    max_y = 0
    node = Node(0, 0, 0, None)
    for move in path:
        node = next(node, move)
        max_x = max([max_x, abs(node.x)])
        max_y = max([max_y, abs(node.y)])
    return node, max_x, max_y


def next(node, move):
    if move == "n":
        node.y += 2
    elif move == "s":
        node.y -= 2
    elif move == "ne":
        node.x += 1
        node.y += 1
    elif move == "nw":
        node.x -= 1
        node.y += 1
    elif move == "se":
        node.x += 1
        node.y -= 1
    elif move == "sw":
        node.x -= 1
        node.y -= 1
    else:
        print("ERROR : unknown move ", move)
    return node


def a_star(final_node, upper_bound):

    # first implementation of a A* algorithm
    origin = Node(0, 0, 0, None)
    open_nodes = [origin]
    closed_nodes = []

    time_sort = 0
    time_search = 0
    time_add = 0
    # possible futur improvement : searching in a cone
    # Now : we limit the search in a quadrant
    while open_nodes:

        timer = time()
        open_nodes.sort(key=lambda n: n.heuristic_value, reverse=True)
        time_sort += time() - timer

        current_node = open_nodes[-1]
        open_nodes = open_nodes[:-1]

        # Stopping criterion
        if current_node == final_node:
            print(time_sort, "  ", time_search, "   ", time_add)
            return current_node.dist

        for neigh in current_node.neighbors():

            if neigh.is_valid(final_node):
                # print("     try ", neigh.x, "  ", neigh.y,
                #      "  ", neigh.heuristic(final_node))
                neigh.heuristic(final_node)
                timer = time()
                if neigh in open_nodes:
                    open_nodes[open_nodes.index(neigh)].update_path(
                        neigh, final_node)
                    time_search += time() - timer
                elif neigh in closed_nodes:
                    closed_nodes[closed_nodes.index(
                        neigh)].update_path(neigh, final_node)
                    time_search += time() - timer
                else:
                    if neigh.dist <= upper_bound:
                        neigh.heuristic(final_node)
                        open_nodes.append(neigh)
                        time_add += time() - timer

        closed_nodes.append(current_node)


def is_open(map, node):
    return map[node.x][node.y].open


def is_closed(map, node):
    return map[node.x][node.y].closed


def is_new(map, node):
    return not is_open(map, node) and not is_closed(map, node)


def a_star_map(final_node, map_of_nodes):
    '''
    Focus the search in the positive quadrant, by symetry
    '''
    map_of_nodes[0][0].dist = 0

    # open_nodes contains the coordinates of the open nodes
    open_nodes = [(0, 0)]

    time_sort = 0
    time_search = 0
    while open_nodes:

        timer = time()
        open_nodes.sort(
            key=lambda n: map_of_nodes[n[0]][n[1]].heuristic_value, reverse=True)
        time_sort += time() - timer

        current_node = map_of_nodes[open_nodes[-1][0]][open_nodes[-1][1]]
        open_nodes = open_nodes[:-1]
        # Stopping criterion
        if current_node == final_node:
            #print(time_search + time_sort)
            return current_node.dist

        timer = time()
        for neigh in current_node.neighbors():
            if neigh.is_valid(final_node):

                map_of_nodes[neigh.x][neigh.y].update_path(neigh, final_node)

                if is_new(map_of_nodes, neigh):
                    open_nodes.append((neigh.x, neigh.y))

        time_search += time() - timer


if __name__ == '__main__':

    input_data = open(argv[1], 'r')
    data = input_data.readline().rstrip('\n').split(',')
    input_data.close()

    final_node, max_x, max_y = compute_final_node(data)
    print("Searching for path to ", final_node.x, "  ", final_node.y)

    # 1. heuristic to have a bound pn the path value
    # going straight in a diagonal direction, then when
    # the current node have same x has the final one,
    # going up or down to reach the final node
    bound = abs(final_node.x) + abs(abs(final_node.x / 2) - abs(final_node.y))
    print("bound : ", bound)

    timer = time()
    print("Part 1 : ", a_star(final_node, bound))
    print("with lists of nodes : %-5.3fs\n" % (time() - timer))

    map_of_nodes = []
    # As we have an hexagonal map, many nodes in map_of_nodes are useless
    for i in range(abs(max_x) + 1):
        map_of_nodes.append([])
        for j in range(abs(max_y) + 1):
            map_of_nodes[i].append(Node(i, j, 1e6, None))

    timer = time()
    print("Part 1 : ", a_star_map(final_node, map_of_nodes))
    print("with map : %-5.3fs\n" % (time() - timer))

    print()
    print("Part 2 :")
    print("Max x : ", max_x, "  max y : ", max_y)
    # Part 2 :
    # launching A* on each reached node
    print("N moves : ", len(data))
    current_node = Node(0, 0, 0, None)
    farther = a_star_map(final_node, map_of_nodes)
    k = 0
    for move in data:
        current_node = next(current_node, move)
        upper_bound = abs(current_node.x) + \
            abs(abs(current_node.x / 2) - abs(current_node.y))
        if upper_bound > farther:
            val = a_star_map(
                Node(abs(current_node.x), abs(current_node.y), 0, None), map_of_nodes)
            if val > farther:
                farther = val
        k += 1
        if k % 100 == 0:
            print(k, "    ",  farther)
    print("Part 2 : ", farther)
