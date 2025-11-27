🟩 1. DFS / Backtracking on Graphs

Explore all nodes, detect cycles, or count connected components.

Common Problems

Number of Islands

Clone Graph

Surrounded Regions

Course Schedule (DFS version)

Word Search

Redundant Connection II (DFS for cycles)

Pattern

Recursive DFS function on nodes

Track visited nodes

Useful for exploring connected components, paths, and cycles

🟦 2. BFS / Level Order / Shortest Path

Explore neighbors level by level, often to find shortest distance or min steps.

Common Problems

Rotten Oranges

Shortest Path in Binary Matrix

Walls and Gates

Word Ladder / Word Ladder II

Minimum Knight Moves / Minimum Jumps

Pattern

Queue for BFS

Level-order traversal using for _ in range(len(queue))

Track visited nodes to prevent cycles

🟥 3. Union-Find / Disjoint Set

Detect cycles, count connected components, or manage merging.

Common Problems

Number of Connected Components in an Undirected Graph

Redundant Connection

Redundant Connection II

Accounts Merge

Graph Valid Tree

Similar String Groups

Pattern

find(x) and union(x, y) operations

Path compression and union by rank for efficiency

Useful for dynamic connectivity

🟨 4. Topological Sort / DAG

Order nodes respecting dependencies.

Common Problems

Course Schedule I & II

Alien Dictionary

Minimum Height Trees

Sequence Reconstruction

Pattern

DFS post-order (reverse for topological order)

BFS / Kahn’s algorithm using in-degree array

Detect cycles for validity

🟪 5. Shortest Path / Weighted Graph

Use BFS for unweighted graphs, Dijkstra / Bellman-Ford for weighted.

Common Problems

Network Delay Time

Cheapest Flights Within K Stops

Minimum Cost to Reach Destination

Path With Maximum Minimum Value

Shortest Bridge

Pattern

BFS for unweighted

Min-heap / Priority Queue for Dijkstra

Edge relaxation for weighted graphs

🟫 6. Minimum Spanning Tree / Greedy

Find minimum spanning tree in weighted graphs.

Common Problems

Min Cost to Connect All Points

Connecting Cities With Minimum Cost

Reduce Cost to Connect Network

Pattern

Kruskal’s algorithm (Union-Find + sort edges)

Prim’s algorithm (Priority Queue + adjacency list)

🟧 7. Graph Coloring / Bipartite

Check if a graph can be colored or partitioned.

Common Problems

Is Graph Bipartite?

Possible Bipartition

Redundant Connection II (detect cycles with directed graph)

Pattern

DFS / BFS to assign colors

Check conflicts for bipartite property

Often combined with cycle detection

🟩 8. Grid Graphs

Treat a 2D grid as a graph; neighbors are up/down/left/right.

Common Problems

Number of Islands

Surrounded Regions

Shortest Path in Binary Matrix

Rotten Oranges

Max Area of Island

Pacific Atlantic Water Flow

Pattern

DFS/BFS in four directions

Track visited

Often edge constraints (0 ≤ x < m, 0 ≤ y < n)

⭐ Top 20 Graph Patterns / Problems (Interview Must-Know)

Number of Islands (DFS/BFS)

Clone Graph (DFS/BFS)

Course Schedule (Topological Sort)

Word Ladder (BFS)

Redundant Connection (Union-Find)

Accounts Merge (Union-Find)

Network Delay Time (Dijkstra)

Min Cost to Connect All Points (MST / Prim / Kruskal)

Alien Dictionary (Topological Sort)

Surrounded Regions (DFS/BFS)

Rotten Oranges (BFS)

Graph Valid Tree (Union-Find / DFS)

Cheapest Flights Within K Stops (BFS / Dijkstra)

Pacific Atlantic Water Flow (DFS/BFS on grids)

Shortest Bridge (BFS on grid)

Minimum Height Trees (BFS / Topological sort on trees)

Redundant Connection II (Union-Find + DFS)

Possible Bipartition (Graph Coloring / BFS)

Max Area of Island (DFS/BFS)

Number of Connected Components (Union-Find / DFS)
