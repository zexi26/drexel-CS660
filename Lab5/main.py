"""
# CS660 Lab 5
## Collaborators
- Evan Lavender
- Merlin Cherian
- Saffat Hasan
- Zexi Yu

## Usage

```bash
spark-submit --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11 main.py
```

"""

import io
from contextlib import redirect_stdout

import handout
from graphframes import GraphFrame
from pyspark.shell import sqlContext

doc = handout.Handout("handout")

""" ## Helper functions """


def print(message):
    """ Overwrite print in this context """
    redirect_to_handout(message)


def redirect_to_handout(message):
    doc.add_text(message)


def display_graph(item):
    # Redirects Standard Out to the document
    with io.StringIO() as buf, redirect_stdout(buf):
        item.show()
        redirect_to_handout(buf.getvalue())


def get_pagerank_dictionary(graph):
    dictionary = {}
    for row in graph.vertices.collect():
        node_id = int(row['id'])
        node_rank = float(row['pagerank'])

        dictionary[node_id] = node_rank

    # Make sure the rank scores add up to 1
    total = sum(dictionary.values())
    for key in dictionary:
        dictionary[key] /= total

    return dictionary


def pretty_print_pagerank(graphframes, google):
    """ Prints a pretty chart with Google, Graphframes, and the Deltas """
    # Divide by total to match Google
    print("+-------+---------------------+")
    print("|Google\t|GraphFrames\t|Delta|")
    print("+-------+---------------------+")
    for key in google:
        goog = google[key]
        g_frames = graphframes_pagerank[key]
        print("|{}\t|{:.3f}\t\t|{:.3f}|".format(goog, g_frames, abs(goog - g_frames)))
    print("+-------+---------------------+")


""" ## Create some edges and vertices to match Fig 2.1 in the paper """
vertices = sqlContext.createDataFrame([
    (1,),
    (2,),
    (3,),
    (4,)],
    ["id"])

edges = sqlContext.createDataFrame([
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
    (3, 1),
    (4, 1),
    (4, 3)],
    ["src", "dst"])

graph = GraphFrame(vertices, edges)

""" ## Show Vertices """
display_graph(graph.vertices)
doc.show()

""" ## Show Edges """
display_graph(graph.edges)
doc.show()

""" ## Show Degrees (Sum of in and out degrees by node) """
display_graph(graph.degrees)
doc.show()

""" ## Get pagerank using m=0.15 and tolerance=0.01
"""
pr = graph.pageRank(resetProbability=0.15, tol=0.01)

""" ### look at the pagerank score for every vertex """
display_graph(pr.vertices)
doc.show()

""" ### look at the weight of every edge
"""
display_graph(pr.edges)
doc.show()


""" We can compare the results as follows: """
# GraphFrames rankings sum to N where N is the number of nodes
graphframes_pagerank = get_pagerank_dictionary(pr)

# Google rankings sum to 1
google_pagerank = {
    1: 0.368,
    2: 0.142,
    3: 0.288,
    4: 0.202
}

pretty_print_pagerank(graphframes_pagerank, google_pagerank)
doc.show()

""" As we can see the results of both algorithms are quite similar """

""" ## Create some edges and vertices to match Fig 2.2 in the paper """
fig_2_2_vertices = sqlContext.createDataFrame([
    (1,),
    (2,),
    (3,),
    (4,),
    (5,)],
    ["id"])

fig_2_2_edges = sqlContext.createDataFrame([
    (1, 2),
    (2, 1),
    (3, 4),
    (4, 3),
    (5, 3),
    (5, 4)],
    ["src", "dst"])

fig_2_2_graph = GraphFrame(fig_2_2_vertices, fig_2_2_edges)


pr = fig_2_2_graph.pageRank(resetProbability=0.15, tol=0.01)

""" ### look at the pagerank score for every vertex """
display_graph(pr.vertices)
doc.show()

""" We can compare the results as follows: """
graphframes_pagerank = get_pagerank_dictionary(pr)

# Google rankings sum to 1
google_pagerank = {
    1: 0.2,
    2: 0.2,
    3: 0.285,
    4: 0.285,
    5: 0.03
}

pretty_print_pagerank(graphframes_pagerank, google_pagerank)
doc.show()
