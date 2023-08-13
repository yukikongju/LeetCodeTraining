#  https://leetcode.com/problems/rotate-function/description/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # solution: F(n+1) = F(n) + sum(nums) - len(nums) * nums[i]

        f0 = sum([i*num for i, num in enumerate(nums)])
        total = sum(nums)
        prev, result = f0, f0

        for i in range(len(nums)-1, 0, -1):
            current = prev + total - len(nums) * nums[i]
            result = max(result, current)
            prev = current
        
        return result
