class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1 and n == 1: 
            return [[1]]
        else:
            combinations = []
            self.findCombinations(combinations, n, k, [], 1)
            return combinations
        
    def findCombinations(self, combinations, n, k, v, c):
        if len(v) == k:
            combinations.append(v)
        else:
            for i in range(c, n+1):
                w = v + [i]
                self.findCombinations(combinations, n, k, w, i+1)
            
