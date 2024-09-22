#  https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # solution: 

        # base case
        if len(nums) < 2:
            return 0

        nums.sort()
        longest = 0
        for i in range(len(nums) - 1):
            longest = max(longest, nums[i+1] - nums[i])
        return longest
        
