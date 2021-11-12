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
        self.heuristic_value = 0
        self.closed = False
        self.open = False

    def heuristic(self, target_node):
        self.heuristic_value = self.dist + \
            ((self.x - target_node.x)**2 + (self.y - target_node.y)**2)

    def update_path(self, node):
        if self.dist > node.dist:
            self.father = node.father
            self.dist = node.dist

    def neighbors(self):
        yield(Node(self.x,      self.y + 1,     self.dist + 1, self))
        yield(Node(self.x,      self.y - 1,     self.dist + 1, self))
        yield(Node(self.x + 1,  self.y + 0.5,   self.dist + 1, self))
        yield(Node(self.x + 1,  self.y - 0.5,   self.dist + 1, self))
        yield(Node(self.x - 1,  self.y + 0.5,   self.dist + 1, self))
        yield(Node(self.x - 1,  self.y - 0.5,   self.dist + 1, self))

    def is_valid(self, final_node):
        '''
        A node is valid if it is in the same quadrant as the final node
        which means same sign of x and y, which is equivalent to "the product is positive"
        '''
        return self.x * final_node.x >= 0 and self.y * final_node.y >= 0

    def __contains__(self, node):
        return self.x == node.x and self.y == node.y

    def __eq__(self, node):
        return self.x == node.x and self.y == node.y


def compute_final_node(path):
    '''
    Starting from origin (0, 0), following the path to compute
    the coordinates of the finale node
    path : a list of moves
    '''
    node = Node(0, 0, 0, None)
    for move in path:
        node = next(node, move)
    return node


def next(node, move):
    if move == "n":
        node.y += 1
    elif move == "s":
        node.y -= 1
    elif move == "ne":
        node.x += 1
        node.y += 0.5
    elif move == "nw":
        node.x -= 1
        node.y += 0.5
    elif move == "se":
        node.x += 1
        node.y -= 0.5
    elif move == "sw":
        node.x -= 1
        node.y -= 0.5
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
                    open_nodes[open_nodes.index(neigh)].update_path(neigh)
                    time_search += time() - timer
                elif neigh in closed_nodes:
                    closed_nodes[closed_nodes.index(neigh)].update_path(neigh)
                    time_search += time() - timer
                else:
                    if neigh.dist <= upper_bound:
                        neigh.heuristic(final_node)
                        open_nodes.append(neigh)
                        time_add += time() - timer

        closed_nodes.append(current_node)


if __name__ == '__main__':

    input_data = open(argv[1], 'r')
    data = input_data.readline().rstrip('\n').split(',')
    input_data.close()

    final_node = compute_final_node(data)
    print("Searching for path to ", final_node.x, "  ", final_node.y)

    # 1. heuristic to have a bound pn the path value
    # going straight in a diagonal direction, then when
    # the current node have same x has the final one,
    # going up or down to reach the final node
    bound = abs(final_node.x) + abs(abs(final_node.x / 2) - abs(final_node.y))
    print("bound : ", bound)

    timer = time()
    print("Part 1 : ", a_star(final_node, 1e6))
    print("without heuristic : %-5.3fs" % (time() - timer))

    timer = time()
    print("Part 1 : ", a_star(final_node, bound))
    print("with    heuristic : %-5.3fs" % (time() - timer))

    # Part 2 :
    # launching A* on each reached node
    print("N moves : ", len(data))
    current_node = Node(0, 0, 0, None)
    farther = a_star(final_node, bound)
    k = 0
    for move in data:
        current_node = next(current_node, move)
        upper_bound = abs(current_node.x) + \
            abs(abs(current_node.x / 2) - abs(current_node.y))
        if upper_bound > farther:
            val = a_star(current_node, 1e6)
            if val > farther:
                farther = val
            if k % 100 == 0:
                print(k, "    ",  farther)

        k += 1
    print("Part 2 : ", farther)
