#  https://leetcode.com/problems/find-the-most-competitive-subsequence/description/

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # solution: Greedy + Stack
        # we want to make the stack such that num[i] <= nums[i+1]

        # --- 
        stack = []
        attempts = len(nums) - k
        for num in nums:
            while stack and num < stack[-1] and attempts > 0:
                attempts -= 1
                stack.pop()
            stack.append(num)
        
        # ---
        return stack[:k]
