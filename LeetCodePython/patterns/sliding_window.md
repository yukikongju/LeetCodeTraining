# Pattern - Sliding Window

- Fixed Window Size:
    * Involves maintaining a fixed-size window as you slide it through the array.
    * Common problems: "Maximum Sum Subarray of Size K," "Longest Substring with At Most K Distinct Characters."

- Variable Window Size:
    * The window size can change based on certain conditions or constraints.
    * Common problems: "Minimum Size Subarray Sum," "Longest Substring Without Repeating Characters."

- Two Pointers Approach:
    * Uses two pointers to define the window's boundaries and optimally move them as you iterate.
    * Common problems: "Container With Most Water," "Trapping Rain Water."

- Sliding Window with Hash Map/Counter:
    * Involves using a hash map or counter to track the frequency of elements within the window.
    * Common problems: "Longest Substring with At Most K Distinct Characters," "Minimum Window Substring."

- Sliding Window with Prefix Sum:
    * Utilizes a prefix sum array to optimize calculations within the sliding window.
    * Common problems: "Subarray Sum Equals K," "Minimum Size Subarray Sum."

- Sliding Window with Double-ended Queue (Deque):
    * Uses a deque data structure to maintain elements within the window.
    * Common problems: "Sliding Window Maximum," "Minimum Swaps to Make Strings Equal."

- Sliding Window with Bit Manipulation:
    * Involves using bitwise operations to efficiently perform calculations within the window.
    * Common problems: "Maximum XOR of Two Numbers in an Array."

- Sliding Window with String Matching:
    * Applying sliding window techniques to string matching problems.
    * Common problems: "Permutation in String," "Minimum Window Substring."

- Sliding Window with Invariants:
    * Involves defining and maintaining certain invariants while adjusting the window.
    * Common problems: "Longest Subarray with Ones After Replacement," "Max Consecutive Ones III."

- Sliding Window with Backtracking:
    * Combines the sliding window approach with backtracking to solve complex problems.
    * Common problems: "Substring with Concatenation of All Words."

- Sliding Window with Custom Conditions:
    * Solving problems with unique conditions or constraints that require sliding window techniques.
    * Common problems: "Minimum Window Substring," "Fruit Into Baskets."

**Template for sliding window**

```{python}
for right in range(n):
    while nums[left] > max_right[right]:
	left += 1
    res = max(res, right - left)
```

