🟩 1. Classic Binary Search

Search in sorted arrays or lists.

✔ Must-Solve

Binary Search (LeetCode 704)

First Bad Version

Find First and Last Position of Element in Sorted Array

Search in Rotated Sorted Array

Search in Rotated Sorted Array II

Core Pattern

left = 0, right = n-1

mid = left + (right - left) // 2

Adjust left / right based on comparison

🟦 2. Search for Bounds / Extremes

Find first / last occurrence, floor / ceiling, or extreme values.

✔ Must-Solve

Find Minimum in Rotated Sorted Array

Find Peak Element

Median of Two Sorted Arrays

Kth Smallest Element in a Sorted Matrix

Split Array Largest Sum

Core Pattern

Modify binary search to move towards first or last valid position

Condition may not be exact equality

🟥 3. Search in Rotated / Shifted Arrays

Arrays that are sorted but rotated.

✔ Must-Solve

Search in Rotated Sorted Array

Find Minimum in Rotated Sorted Array

Search in Rotated Sorted Array II (with duplicates)

Core Pattern

Identify sorted half

Decide which half to continue searching

Works for log(n) runtime

🟨 4. Binary Search on Answer / Decision Problems

Search for the smallest / largest feasible answer.

✔ Must-Solve

Capacity To Ship Packages Within D Days

Koko Eating Bananas

Split Array Largest Sum

Minimum Time to Complete Trips

Median of Two Sorted Arrays

Core Pattern

Define search space [low, high] for answer

Check feasibility function isValid(mid)

Narrow search to satisfy constraints

🟪 5. Floating Point / Precision Binary Search

Search in continuous space with tolerance.

✔ Must-Solve

Sqrt(x) (with precision)

Nth Root of a Number

Koko Eating Bananas variant with fractional hours

Core Pattern

Use epsilon as stopping condition (high - low > 1e-6)

Adjust mid and check feasibility

🟫 6. Two Pointers + Binary Search

Combine binary search with two pointers or sliding window.

✔ Must-Solve

Search Pair with Given Sum in Sorted Array

3Sum / 3Sum Closest (binary search after sorting)

Find Right Interval

Core Pattern

Fix one element

Use binary search on remaining subarray

🟧 7. Advanced / Template Problems

Problems requiring clever usage of binary search.

✔ Must-Solve

Aggressive Cows / Magnetic Force Between Two Balls

Capacity To Ship Packages Within D Days

Split Array Largest Sum

Minimum Days to Make m Bouquets

Kth Smallest Element in Sorted Matrix / Multiplication Table

Core Pattern

Binary search on answer space, not array index

Feasibility function is key

⭐ Top 15 Binary Search Problems (Interview Must-Know)

Binary Search (standard)

First / Last Occurrence in Sorted Array

Search in Rotated Sorted Array

Find Minimum in Rotated Sorted Array

Median of Two Sorted Arrays

Kth Smallest Element in Sorted Matrix

Split Array Largest Sum

Capacity To Ship Packages Within D Days

Koko Eating Bananas

Search in Rotated Sorted Array II

Aggressive Cows / Magnetic Force Between Balls

Minimum Days to Make m Bouquets

Find Peak Element

Search Right Interval

Sqrt(x) or Nth Root of a Number
