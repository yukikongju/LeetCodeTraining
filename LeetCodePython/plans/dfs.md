# DFS

🟦 1. Graph Traversal Basics

These teach pure DFS mechanics: visited sets, recursion, adjacency lists.

✔ Core Problems
Number of Connected Components
Graph Valid Tree
Find if Path Exists in Graph
All Paths From Source to Target
Course Schedule (Detect Cycle in Directed Graph)

Concepts
adjacency list
visited set vs recursion stack
detecting cycles (undirected vs directed)

🟩 2. Matrix / Grid DFS (Most Common in Interviews)

These build intuition for DFS on 2D grids.

✔ Must-Solve
Number of Islands
Max Area of Island
Flood Fill
Surrounded Regions
Rotting Oranges (BFS main, but DFS version exists)
Word Search
Word Search II (Hard) ← uses Trie + DFS

Concepts
boundary checks
modifying grid vs using visited
exploring 4 or 8 directions

🟧 3. Backtracking DFS

Try paths, undo moves, explore all possibilities.

✔ Fundamental
Permutations
Permutations II
Combinations
Combination Sum
Combination Sum II
Letter Combinations of a Phone Number
Subsets
Subsets II
N Queens
Sudoku Solver (elite DFS + constraints)

Concepts
path list
backtracking (append → recurse → pop)
decision tree traversal

🟥 4. Tree DFS

Recursive tree DFS is foundational.

✔ Essential Problems
Binary Tree Inorder Traversal
Binary Tree Preorder Traversal
Binary Tree Postorder Traversal
Diameter of a Binary Tree
Path Sum / Path Sum II
Lowest Common Ancestor (LCA)
Serialize and Deserialize Binary Tree (uses DFS)
Binary Tree Maximum Path Sum

Concepts
postorder for bottom-up
preorder for top-down
return values vs global state

🟪 5. DFS With State (Memoization / DP on Graphs)

These require DFS + memo caching.

✔ Problems
Longest Increasing Path in a Matrix
Word Break (DFS + memo)
Word Break II
Target Sum
Interleaving String

Concepts
avoid recomputing paths
DFS + caching results in dict[(i, j)]

🟫 6. Trie + DFS Hybrid

Like Word Search II, these use DFS guided by Trie nodes.

✔ Problems
Word Search II
Replace Words (Trie core)
Design Search Autocomplete System

Concepts
DFS prunes huge search space using trie
tracking prefix nodes

🟨 7. DFS on Bitmask / State-Space Search

Harder category, often interview finals.

✔ Problems
Traveling Salesman (TSP) small inputs
Remove Invalid Parentheses
Palindrome Partitioning
Matchsticks to Square
Reconstruct Itinerary (Hierholzer, but DFS version exists)

Concepts
bitmask DP
DFS with pruning
lexicographically smallest path

⭐ The 15 DFS Problems You Must Solve Before Any Interview

If you want a short, high-impact list:
Number of Islands
Flood Fill
Surrounded Regions
Max Area of Island
Word Search
Word Search II
Permutations
Combinations
Subsets II
Combination Sum
N Queens
Sudoku Solver
Diameter of Binary Tree
Longest Increasing Path in Matrix
Course Schedule (cycle detection)



