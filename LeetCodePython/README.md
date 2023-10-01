# LeetCode Solutions in Python

[Blink 75 by Sean Prashad](https://seanprashad.com/leetcode-patterns/)
[NeetCode 150](https://neetcode.io/practice)

## General Tips

**Questions to answer**

1. Explain the algorithm, time and space complexity, alternative, ...
2. Ask yourself follow up questions
3. Frame the question in a real world context

**How to effectively study**

1. Pick a new problem pattern: sliding window, DFS+DP, monotonic stack, ...
2. Check problem resolution for that type of problem
3. Solve that problem by looking at the code template once
4. Solve a bunch of problems following that patterns without looking at answers

## Python Tips

**How to find duplicates in an array**

We use `tupple()` and `set()`


## Types of Problems

**Arrays**

- [X] Running Sum
    * Find the Highest Altitude
- [X] Hashmap + Greedy
    * Minimum Deletions to Make Character Frequencies Unique
- [X] Hashmap: frequency count
    * Minimum Number of People to Teach
- [-] Hashmap: frequency count + Complement
    * Count Good Meals (complement)
- [ ] Two Pointers
- [X] Hard Sliding Window
    * Maximum Number of Vowels in Substring
- [X] Sliding Window - Count Contiguous Subarrays
    * Number of Zero-Filled Subarrays, Number of Smooth Descent Periods
    * Max Consecutive Ones III, SubarrayProductLessThanK
- [X] Palindrome => increment by 2 if letter can be paired
    * Largest Palindromic Number
- [ ] Binary Search
    * Koko eats banana
    * Find Peak Element II (2D)
- [ ] Prefix Sum - Mountain Array
    * Longest Mountain in Array
- [ ] Set + Retry from beginning when adding to set
    * Find All Possible Recipes from Given Supplies
- [-] String Manipulation - Checking previous & number not starting with zeroes
    * Additive Number

**Linked List**

- [ ] fast and slow pointer + Reverse Linked List
    * Maximum Twin Sum of A Linked List


**Trees**

- [X] Tree to Graph
    * Amount of Time for Binary Tree to Be Infected, All Nodes Distance K in Binary Tree
- [X] BFS // Level Order Traversal
    * Binary Tree Right Side View
- [X] DFS: Traverse all nodes with stack
- [ ] DFS: recurrence depth
    * Minimum Fuel Cost to Report to the Capital
- [X] Balanced Tree
    * Balanced Binary Tree
- [-] In-order DFS Traversal
    * Minimum Absolute Difference in BST
    * Kth Smallest Element in a BST
- [X] Preorder Traversal (parent then childs) // Post-order Traversal
    * Count Good Nodes in Binary Tree
- [ ] Lowest Common Ancestor
- [X] Diameter of Tree
    * Diameter of Binary Tree
- [X] Same Tree
    * Subtree of Another Tree
- [-] Find Cousins: BFS-ish
    * Cousins in Binary Tree
- [X] Level Order Traversal + maxHeap
    * Kth Largest Sum in Binary Tree
- [-] Delete Nodes
    * Delete Leaves With a Given Value
- [X] Construct Tree from Traversal
    * Construct Binary Tree from Preorder and Inorder Traversal
    * Construct Binary Tree from Inorder and Postorder Traversal

**Stack**

- [X] Decreasing Monotonic Sequence
    * Daily Temperature
    * Monotone Increasing Digits
- [-] Circular Decreasing Monotonic Sequence
    * Next Greater Number II
- [X] Balanced: Stack + Pointer for last
    * Minimum Swaps to make String Balanced, Minimum Remove to Make Valid Parentheses
- [-] Balanced Parentheses
    * Minimum Insertions to Balance a Parentheses String
- [-] Balanced Parentheses: Forward-Backward Pass
    * Check if a Parentheses String Can Be Valid, Valid Parenthesis String
- [X] Monotonic Stack + HashMap
    * Smallest Subsequence Of Distinct Character, Remove Duplicate Letters
- [ ] PEMDAS
    * Basic Calculator
- [-] pop if equal values
    * Asteroid Collision

**Graphs**

- [X] Graph DFS:
    * Number of Islands, Max Area of Island, Surrounded Regions, Rotting Oranges, Pacific Water Flow
- [X] Graph BFS:
    * Nearest Exit
- [X] Topological Sort // DFS no cycle:
    * Course Schedule, Course Schedule II
- Union Find:
    * 
- [X] Minimum Spanning Tree
    * Minimum Cost to Connect All Points
- [X] Shortest Path: Dijkstra, Bellman-Ford, Floyd-Warshall
    * Network Delay Time
    * Cheapest Flights Within K Stops
    * FindCityWithSmallestNumberOfNeighborsAtThresholdDistance
- [X] Graph BFS + Heap:
    * Swim in Rising Water
- DFS + BFS
- [X] minHeap // maxHeap
    * Find Safest Path in Grid, Reconstruct 2-Row Binary Matrix
- [ ] Eulerian Paths
    * Reconstruct Itinery
- [ ] In-place Manipulation
    * Game of Life

**Dynamic Programming**

- [-] 1D DP
    * Perfect Squares, Ways to Express and Integer as Sum of Powe
- [X] Sol1: max(diago + 1, top, left)
    * Coin Change
- [X] Sol2: [ DFS + caching ] ; [ Backtracking + caching ]
    * Best Time to Buy and Sell Stock with Cooldown
    * Target Sum
    * Longest Increasing Path in Matrix, Number of Increasing Path in a Grid, Maximum Strictly Increasing Cells in a Matrix
- [X] Knapsack 0-1

**Backtracking**

- [-] Backtrack + Memoization:
    * Minimize the Difference Between Target and Chosen Elements
    * Number of Increasing Paths in a grid
- [X] vecteur k prometteur
    * subsets
    * N-queens

**Heap**

- [X] Counts
    * Least Number of Unique Integers after K Removals

**Intervals**

- Insert Intervals, Merge Intervals, Non Overlapping Intervals
    * case 1: not overlapping ; case 2: overlapping: imbricated vs superposed

**Greedy**

- [X] Sort + Greedy
    * Miximum Ice Cream Bars
- [ ] Sum Row/Cols
    * Find Valid Matrix Given Row and Column Sums
- [X] Greedy + Stack
    * Remove K Digits, Find Most Competitive Subsequence
- [ ] Subsequence
    * Increasing Triplet Subsequence


**Bit Manipulation**

- [-] Right Shifting
    * Reverse Bits, 
    * Power of Two: `n&(n-1) == 0`
- [ ] XOR: `a ^ b = c <=> a ^ c = b`
    * Find the Original Array of Prefix XOR
- [ ] Bitwise - In-place
    * Game of Life
- [X] Subsets with Bitmask
    * Subsets, 

**Maths and Geometry**

- [ ] Modulo
    * Bulb Switcher II
    * Ugly Number I/II
- [ ] Addition/Substractions
    * Maximum Score from Removing Stones


## Ressources

- [CMU 15-210: Data Structures Notes](http://www.cs.cmu.edu/afs/cs/academic/class/15210-s15/www/lectures/)
- [NeetCode LeetCode Solutions](https://github.com/neetcode-gh/leetcode/tree/main/python)
- [LeetCode - Google Questions](https://leetcode.com/discuss/interview-question/971009/List-of-2020-interview-question-for-Google)
- [walkccc - LeetCode](https://github.com/walkccc/LeetCode)
- [Strivers A2Z DSA Course](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

