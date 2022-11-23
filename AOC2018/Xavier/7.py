from itertools import chain
from sys import argv


def find_and_print_node_and_balance_weight(total_weights, n, nodes, dico_weights):
    for w in dico_weights:
        # Searching for the node which is the only one with its value
        # this is the node creating unbalance
        if len(dico_weights[w]) == 1:
            unbal_node = dico_weights[w][0]
            print("Unbalance at : ", dico_weights[w][0])
            # The true value of the node depend if it is
            # lower or grater than the others
            if nodes[unbal_node].total_weight == min(total_weights):
                print(
                    "Value : ", nodes[unbal_node].weight
                    + max(total_weights) - min(total_weights))
            else:
                print(
                    "Value : ", nodes[unbal_node].weight
                    - max(total_weights) + min(total_weights))


def find_first_node_unbalanced(total_weights, n, nodes, first_unbalanced):
    # Compute the value the first time unbalanced nodes appear
    if not first_unbalanced:
        # if unbalance occure
        if total_weights and max(total_weights) - min(total_weights) > 0:

            # dict of successors, by total_weight, only two values,
            # as only one node with unbalance
            dico_weights = {
                max(total_weights): [m for m in nodes[n].successors
                                     if nodes[m].total_weight == max(total_weights)],
                min(total_weights): [m for m in nodes[n].successors
                                     if nodes[m].total_weight == min(total_weights)]
            }

            find_and_print_node_and_balance_weight(
                total_weights, n, nodes, dico_weights)

            # First node with unbalance has been found, add it to the list
            # (which will contain only it) so that this will never be called again
            first_unbalanced.append(n)


# Computing total weight in a recursive way
def compute_weight(n, nodes, first_unbalanced):
    total_weights = []
    for m in nodes[n].successors:
        compute_weight(m, nodes, first_unbalanced)
        nodes[n].total_weight += nodes[m].total_weight
        total_weights.append(nodes[m].total_weight)

    find_first_node_unbalanced(total_weights, n, nodes, first_unbalanced)


class Node:
    def __init__(self, name, weight, successors):
        self.weight = weight
        self.name = name
        self.successors = successors
        self.total_weight = weight


if __name__ == '__main__':

    # Part 1

    # nodes : dict{name: Node(name, weight,successors)}
    nodes = {}
    input_data = open(argv[1], 'r')
    for line in input_data:
        name = line.split()[0]
        weight = int(line.split()[1][1:-1])
        successors = [n.rstrip(',') for n in line.rstrip('\n').split()[3:]]
        nodes[name] = Node(name, weight, successors)
    input_data.close()

    # Init node is the only node not appearing as a successor of someone
    names = set([n.name for n in nodes.values()])
    all_successors = set()
    for successors in chain(n.successors for n in nodes.values()):
        for n in successors:
            all_successors.add(n)

    for n in names - all_successors:
        node_init = n
    print("Node init : ", node_init)

    # Part 2
    first_unbalanced = []
    # Compute total weights of nodes with a recursive function starting from init node
    compute_weight(node_init, nodes, first_unbalanced)
