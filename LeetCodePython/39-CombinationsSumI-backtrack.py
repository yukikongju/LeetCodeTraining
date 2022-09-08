#  Link: https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.findCombinations(combinations, candidates, target, [])
        return combinations
    
    def findCombinations(self, combinations, candidates, target, v):
        # we need to call the candidate after the position we are at, otherwise we will repeat
        if sum(v) == target:
            combinations.append(v)
        elif sum(v) < target:
            for i, val in enumerate(candidates):
                w = v + [val]
                self.findCombinations(combinations, candidates[i:], target, w)
                
