# CS 660 Assignment 1
## Collaborators
- Evan Lavender
- Merlin Cherian
- Saffat Hasan
- Zexi Yu

## Output

### PageRank Toy Example - Iteration 1

Node | [PageRank, Adjacency List]
---- | ---
3   |    [0.16666666666666669, [4]]
5    |   [0.30000000000000004, [1, 2, 3]]
2    |   [0.16666666666666669, [3, 5]]
4    |   [0.30000000000000004, [5]]
1    |   [0.06666666666666667, [2, 4]]

### PageRank Toy Example - Iteration 2

Node | [PageRank, Adjacency List]
---- | ---
3    |   [0.18333333333333335, [4]]
5   |    [0.3833333333333334, [1, 2, 3]]
2    |   [0.13333333333333336, [3, 5]]
4    |   [0.2, [5]]
1    |   [0.10000000000000002, [2, 4]]

### PageRank Toy Example - Full Iterations (8)

```bash
python3 driver.py input/graph.txt 5
```

Node | [PageRank, Adjacency List]
---- | ---
2    |   [0.19438740941308597, [3, 5]]
1   |    [0.1808254972595215, [2, 4]]
5    |   [0.21650994537829593, [1, 2, 3]]
4    |   [0.21287259500732425, [5]]
3    |   [0.19540455294177247, [4]]

### PageRank Toy Example w/ Dangling Node - Full Iterations (7)

```bash
python3 driver.py input/graph_dangling.txt 5
```

Node | [PageRank, Adjacency List]
---- | ---
2    |   [0.2001702944644922, [3, 5]]
1   |    [0.18620492507765626, [2, 4]]
5    |   [0.1916359021149219, [1, 2, 3]]
4    |   [0.22077115389347657, []]
3    |   [0.20121769719257815, [4]]