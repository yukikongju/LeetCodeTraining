#  Link: https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        self.findCombinations(combinations, candidates, target, [], 0)
        return combinations
    
    def findCombinations(self, combinations, candidates, target, v, k):
        # we need to check that (1) we iterate to the next candidates (2) not the same as prev (otherwise duplicates) 
        if sum(v) == target:
            combinations.append(v)
        elif sum(v) < target:
            for i in range(k, len(candidates)):
                if i > k and candidates[i] == candidates[i-1]:
                    continue
                w = v + [candidates[i]]
                self.findCombinations(combinations, candidates, target, w, i+1)
                
