#  Link: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else: 
            permutations = []
            self.findPermutations(nums, [], permutations)
            return permutations
    
    def findPermutations(self, nums, vect, permutations):
        if len(nums) == len(vect):
            permutations.append(vect)
        else: 
            for num in nums: 
                if num not in vect: 
                    w = vect + [num]
                    self.findPermutations(nums, w, permutations)
                
            
