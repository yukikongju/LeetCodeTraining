#  Link: https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # cascade solution
        n = len(nums)
        outputs = [[]]
        
        for num in nums: 
            outputs += [current + [num] for current in outputs]
        
        return outputs
            
