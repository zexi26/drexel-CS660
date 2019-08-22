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

""" Show all motifs which satisfy a->b->c """
display_graph(graph.find("(a)-[e]->(b); (b)-[e2]->(a)"))


def display_graph(item):
    # Redirects Standard Out to the document
    with io.StringIO() as buf, redirect_stdout(buf):
        graph.find("(a)-[e]->(b); (b)-[e2]->(a)").show()
        redirect_to_handout(buf.getvalue())


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
graphframes_pagerank = {
    1: 1.4645853473254988,
    2: 0.5777965605200768,
    3: 1.1469145091124107,
    4: 0.8107035830420137
}

# Divide by total to match Google
total = sum(graphframes_pagerank.values())
for key in graphframes_pagerank:
    graphframes_pagerank[key] /= total

# Google rankings sum to 1
google_pagerank = {
    1: 0.368,
    2: 0.142,
    3: 0.288,
    4: 0.202
}

# Pretty Print
print("+-------+---------------------+")
print("|Google\t|GraphFrames\t|Delta|")
print("+-------+---------------------+")
for key in google_pagerank:
    google = google_pagerank[key]
    g_frames = graphframes_pagerank[key]
    print("|{}\t|{:.3f}\t\t|{:.3f}|".format(google, g_frames, abs(google - g_frames)))
print("+-------+---------------------+")
doc.show()

""" As we can see the results of both algorithms are quite similar """
