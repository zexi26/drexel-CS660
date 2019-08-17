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
def display_graph(item):
    # Redirects Standard Out to the document
    with io.StringIO() as buf, redirect_stdout(buf):
        item.show()
        doc.add_text(buf.getvalue())

""" ## Create some edges and vertices """
vertices = sqlContext.createDataFrame([
    (1,),
    (2,),
    (3,),
    (4,)],
    ["id"])

edges = sqlContext.createDataFrame([
    (1, 2),
    (1, 3),
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

""" ## Get pagerank using m=0.15 and tolerance=0.01 """
pr = graph.pageRank(resetProbability=0.15, tol=0.01)

""" ### look at the pagerank score for every vertex """
display_graph(pr.vertices)
doc.show()

""" ### look at the weight of every edge """
display_graph(pr.edges)
doc.show()
