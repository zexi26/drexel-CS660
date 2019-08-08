from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol


class PageRankSimple(MRJob):
    INPUT_PROTOCOL = JSONProtocol

    def mapper(self, node_id, node):
        # node consists of "node_id \t [page_rank, [adjacency_list]]"
        page_rank, adjacency_list = node

        # calculate mass to distribute
        p = page_rank / len(adjacency_list)

        # yield the actual node so it can be used later (in the reducer)
        yield node_id, node

        # yield the mass along with each adjacent node id
        for adjacent_id in adjacency_list:
            yield adjacent_id, p

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
    PageRankSimple.run()
