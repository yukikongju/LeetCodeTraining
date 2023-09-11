#  https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # solution: 
        # we keep track of current minimum value 

        # --- 
        n = len(nums)
        res = [-1 for _ in range(n)]
        smallest = nums[0]
        for i in range(1, n):
            if nums[i] > smallest:
                res[i] = nums[i] - smallest
            smallest = min(nums[i], smallest)
        
        return max(res)
        
