#  Link: https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Sol: sorting and check consecutive values
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
            
            
