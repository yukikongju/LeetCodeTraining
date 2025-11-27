# Dynamic Programming

🟦 0. DP Essentials (Warm-Up)
Learn these patterns first.
✔ Core Basics
Climbing Stairs
Min Cost Climbing Stairs
Fibonacci Number
House Robber
House Robber II
Nth Tribonacci

Concepts
bottom-up table
recursion + memo
base cases

🟩 1. 1-D DP (Linear State)

DP[i] depends on previous few states.

✔ Must-Solve
Maximum Subarray (Kadane)
Delete and Earn
Jump Game
Jump Game II
Longest Increasing Subsequence
Russian Doll Envelopes (LIS 2D)
Partition Equal Subset Sum
Combination Sum IV
Paint Fence

Concepts
transitions in 1D
greedy vs dp
LIS (O(n²) and O(n log n))

🟧 2. 2-D DP (Tables / Grid DP)

Classic interview grid-based DP.

✔ Must-Solve
Unique Paths
Unique Paths II
Minimum Path Sum
Cherry Pickup II (hard)
Dungeon Game
Maximal Square
Longest Common Subsequence (LCS)
Longest Common Substring
Edit Distance
Interleaving String
Distinct Subsequences

Concepts
dp[r][c] tables
string DP
transitions from left/top/diagonal
reverse DP (Dungeon Game)

🟥 3. Knapsack (0/1, Unbounded, Bounded)

Every company tests this.

✔ Must-Solve
0/1 Knapsack
Target Sum
Last Stone Weight II
Coin Change (unbounded)
Coin Change II
Perfect Squares
Combination Sum IV
Ones and Zeroes (2D knapsack)

Concepts
choose vs skip
weights & capacity
multiple constraints (2D)
unbounded vs bounded

🟪 4. DP on Strings

Core LCS-based problems.

✔ Must-Solve
Longest Palindromic Subsequence
Palindromic Substrings
Longest Palindromic Substring
Palindrome Partitioning II
Decode Ways
Regular Expression Matching
Wildcard Matching
Word Break
Word Break II (DFS + memo)

Concepts
substring vs subsequence
palindrome expansions
dp[i][j] on ranges

🟫 5. DP on Trees

Tree DP requires bottom-up reasoning.

✔ Must-Solve
House Robber III
Binary Tree Maximum Path Sum
Diameter of Binary Tree
Count Good Nodes in Binary Tree (top-down DP idea)
Smallest Sufficient Team (bitmask tree DP)
Concepts
solve subproblems of children
return multiple states
postorder DFS

🟨 6. DP on Graphs

Graph-based DP often uses DAG + memo.

✔ Must-Solve
Longest Increasing Path in a Matrix (DFS + memo)
Course Schedule (variation with DP)
Number of Ways to Arrive at Destination
Word Ladder II (DP + BFS)

Concepts
DAG DP
memoizing DFS on graph
longest paths

🟧 7. Bitmask DP

A must for senior-level interviews.

✔ Must-Solve
Traveling Salesman Problem (TSP)
Partition to K Equal Sum Subsets
Smallest Sufficient Team
Matchsticks to Square
Maximum Compatibility Score Sum

Concepts
DP over subsets
bit operations
compressing state to integer

🟥 8. Interval DP

Highly advanced but very common.

✔ Must-Solve
Burst Balloons
Palindrome Partitioning II
Minimum Cost to Merge Stones
Strange Printer

Concepts
dp[l][r] over ranges
exploring partitions
optimal substructure over intervals

🟩 9. Game Theory DP

Two-player optimal strategy problems.

✔ Must-Solve
Stone Game
Stone Game II
Predict the Winner
Nim Game
Concepts
dp[l][r] representing score difference
zero-sum games

⭐ Top 20 DP Problems (Essential Set)
Climbing Stairs
House Robber
House Robber II
Coin Change
Coin Change II
Target Sum
0/1 Knapsack
Partition Equal Subset Sum
Longest Increasing Subsequence
Unique Paths
Minimum Path Sum
Edit Distance
Longest Common Subsequence
Decode Ways
Word Break
Palindromic Substrings
Longest Palindromic Subsequence
Longest Increasing Path in a Matrix
Burst Balloons
Stone Game
