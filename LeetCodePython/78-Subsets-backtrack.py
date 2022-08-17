#  Link: https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        else:
            subsets = []
            self.findSubsets(nums, [], 0, subsets)
            return subsets
            
    def findSubsets(self, nums, vect, k, subsets):
        subsets.append(vect)
        for i in range(k, len(nums)): 
            w = vect + [nums[i]]
            self.findSubsets(nums, w, i+1, subsets)
            
