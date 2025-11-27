# Backtracking

🟩 1. Subsets / Combinations (choose or skip)

These follow the pattern: make a choice → recurse → undo choice.

✔ Must-Solve

Subsets

Subsets II (with duplicates)

Combinations (n choose k)

Combination Sum

Combination Sum II

Combination Sum III

Letter Case Permutation

Generate Parentheses

Palindrome Partitioning

Increasing Subsequences

Core Pattern
def backtrack(i, path):
    if end_condition:
        ans.append(path)
    for choice in choices:
        path.append(choice)
        backtrack(next, path)
        path.pop()

🟦 2. Permutations (arrange items)

These involve used[] arrays or in-place swaps.

✔ Must-Solve

Permutations

Permutations II (with duplicates)

Letter Tile Possibilities

Reconstruct Itinerary

Unique Paths with Obstacles (backtracking variant)

Next Permutation (not backtracking but related concept)

Strobogrammatic Numbers

Core Pattern
used = [False]*len(nums)

def backtrack(path):
    if len(path) == len(nums):
        ans.append(path[:])
    for i in range(len(nums)):
        if used[i]: continue
        used[i] = True
        backtrack(path + [nums[i]])
        used[i] = False

🟥 3. String Building / Decision Trees

Choose characters to build strings.

✔ Must-Solve

Generate Parentheses

Letter Combinations of a Phone Number

Restore IP Addresses

Decode Ways (backtracking version)

Word Pattern Match

Additive Number

🟨 4. Board Search / DFS Matrix Backtracking

These are signature backtracking interview problems.

✔ Must-Solve

Word Search

Word Search II (Trie + backtracking)

Sudoku Solver

N-Queens

N-Queens II

Rat in a Maze

Knight’s Tour

Connected Components (backtracking/pseudo-DFS)

Unique Paths III (walk all nodes exactly once)

Core Pattern
def dfs(r, c):
    if invalid: return
    mark
    for each direction:
        dfs(...)
    unmark

🟪 5. Partitioning / Splitting Problems

These require branching decisions about how to cut sequences.

✔ Must-Solve

Palindrome Partitioning

Partition to K Equal Sum Subsets

Matchsticks to Square

Split Array Into Fibonacci Sequence

Additive Number

Expression Add Operators

🟫 6. Constraint Satisfaction Problems (CSP)

Backtracking is perfect for problems with hard constraints.

✔ Must-Solve

Sudoku Solver (ultimate CSP)

N-Queens (use sets for pruning)

Graph Coloring Problem

Map Coloring

Cryptarithmic Puzzles (SEND + MORE = MONEY)

Boolean Satisfiability (general backtracking)

🟧 7. Optimization Backtracking

Backtrack through possibilities but keep track of best score.

✔ Must-Solve

Maximum Score Words Formed by Letters

Shopping Offers

Beautiful Arrangement

Increasing Subsequences

Smallest Sufficient Team (bitmask + backtracking)

Max Score After K Operations

🟦 8. Backtracking + Bitmasking

Useful for medium-hard FAANG-level problems.

✔ Must-Solve

Partition to K Equal Sum Subsets (bitmask DP + backtracking)

Maximum Compatibility Score

Smallest Sufficient Team

Count Numbers With Unique Digits

Letter Tile Possibilities

🟣 9. Backtracking + Sorting to prune

Sorting allows you to prune duplicates or break early.

✔ Must-Solve

Combination Sum II

Permutations II

Subsets II

Matchsticks to Square

Partition to K Equal Sum Subsets

⭐ Top 20 Backtracking Problems (Essential Set)

If you're preparing for interviews, solve these:

Subsets

Subsets II

Combinations

Combination Sum

Combination Sum II

Generate Parentheses

Letter Combinations of Phone Number

Permutations

Permutations II

Palindrome Partitioning

Word Search

Sudoku Solver

N-Queens

Word Search II

Restore IP Addresses

Partition to K Equal Sum Subsets

Expression Add Operators

Matchsticks to Square

Unique Paths III

Reconstruct Itinerary
