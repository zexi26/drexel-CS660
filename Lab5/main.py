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
with io.StringIO() as buf, redirect_stdout(buf):
    graph.vertices.show()
    doc.add_text(buf.getvalue())
doc.show()

""" ## Show Edges """
with io.StringIO() as buf, redirect_stdout(buf):
    graph.edges.show()
    doc.add_text(buf.getvalue())
doc.show()
