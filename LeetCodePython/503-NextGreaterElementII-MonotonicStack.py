#  https://leetcode.com/problems/next-greater-element-ii/description/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # solution: Monotonic stack - O(n)
        # two pass: https://www.youtube.com/watch?v=WLrA8X66mQs

        # --- 
        results = [-1 for _ in range(len(nums))]
        stack = [] # idx

        # --- 
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                results[stack.pop()] = num
            stack.append(i)

        # --- if greater number is at the left
        for i, num in enumerate(nums):
            if i == stack[-1]:
                break
            while stack and nums[stack[-1]] < num:
                results[stack.pop()] = num

        return results

