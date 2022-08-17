#  Link: https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtracking solution
        if len(nums) == 1:
            return [[], nums]
        else: 
            subsets = []
            self.findSubsets(nums, [], 0, subsets)
            return subsets
    
    def findSubsets(self, nums, vect, k, subsets):
        if vect not in subsets:
            subsets.append(vect)
        for i in range(k, len(nums)):
            w = vect + [nums[i]]
            self.findSubsets(nums, w, i+1, subsets)
        
