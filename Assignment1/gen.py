import random
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        num_nodes = 5
    else:
        num_nodes = int(sys.argv[1])

    print("Making a random graph with %s nodes" % num_nodes)

    with open("./gen/gen_graph.txt", "w") as file:
        for n in range(1, num_nodes + 1):
            adjacency_list = [1 / num_nodes]

            while len(adjacency_list) == 1:
                adjacency_list.extend([random.sample(range(1, num_nodes + 1), random.choice(range(0, num_nodes)))])

                if n in adjacency_list[1:]:
                    adjacency_list[1:].remove(n)

            file.write("%s\t%s\n" % (n, adjacency_list))
