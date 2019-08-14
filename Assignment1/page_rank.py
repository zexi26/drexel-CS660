import ast

from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol


class DanglingJob(MRJob):
    """Computes modified page rank value"""

    INPUT_PROTOCOL = JSONProtocol

    def configure_args(self):
        super(DanglingJob, self).configure_args()

        self.add_passthru_arg("dangling_nodes", type=list, help="List of dangling nodes and their rank")

    def mapper(self, node_id, node):
        # get any dangling nodes
        input = self.options.dangling_nodes

        num_nodes = int(input[0])
        random_surfer = float(input[1])
        dangling_nodes = ast.literal_eval(input[2])
        dangling_mass = 0
        page_rank = float(node[0])

        # add mass of dangling node
        for dangling_id, mass in dangling_nodes.items():
            mass = (float(mass) / 1000000)
            dangling_mass += (mass / num_nodes)

        # compute modified page rank
        node[0] = random_surfer * (1 / num_nodes) + (1 - random_surfer) * (dangling_mass + page_rank)

        yield node_id, node


class PageRankJob(MRJob):
    """Computes raw page rank value and tracks dangling nodes"""

    INPUT_PROTOCOL = JSONProtocol

    def mapper(self, node_id, node):
        # input consists of "node_id \t [page_rank, [adjacency_list]]"
        page_rank, adjacency_list = node

        # yield the actual node so it can be used later (in the reducer)
        yield node_id, node

        # calculate mass to distribute
        if len(adjacency_list) > 0:
            p = page_rank / len(adjacency_list)

            # yield the mass along with each adjacent node id
            for adjacent_id in adjacency_list:
                yield adjacent_id, p
        else:
            # keep track of dangling nodes
            self.increment_counter("dangling_nodes", node_id, int(page_rank * 1000000))

    def reducer(self, node_id, values):
        node = None
        page_rank = 0

        for value in values:
            # if the value is a list, save that as the node
            if isinstance(value, list):
                node = value
            else:
                page_rank += value

        node[0] = page_rank
        yield node_id, node


if __name__ == "__main__":
    PageRankJob.run()
