#  Link: https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = []
        self.findPermutations(s, '', 0, permutations)
        return permutations
    
    def findPermutations(self, s, vect, k, permutations):
        if len(vect) == len(s):
            permutations.append(vect)
        else: 
            char = s[k]
            if char.isalpha():
                for case in [char.upper(), char.lower()]:
                    w = vect + case
                    self.findPermutations(s, w, k+1, permutations)
            else: 
                w = vect + char
                self.findPermutations(s, w, k+1, permutations)
