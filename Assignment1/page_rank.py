import ast

from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol


class DanglingJob(MRJob):
    INPUT_PROTOCOL = JSONProtocol

    def configure_args(self):
        super(DanglingJob, self).configure_args()

        self.add_passthru_arg("dangling_nodes", type=list, help="List of dangling nodes and their rank")

    def mapper(self, node_id, node):
        # get the nodes!
        input = self.options.dangling_nodes

        num_nodes = int(input[0])
        dangling_nodes = ast.literal_eval(input[1])

        for page_rank, dangling_id in dangling_nodes.items():
            node[0] += (float(page_rank) / num_nodes)

        yield node_id, node


class PageRankJob(MRJob):
    INPUT_PROTOCOL = JSONProtocol

    def mapper(self, node_id, node):
        # node consists of "node_id \t [page_rank, [adjacency_list]]"
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
            # we got us a dangling node here
            self.increment_counter("dangling_nodes", page_rank, node_id)

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
