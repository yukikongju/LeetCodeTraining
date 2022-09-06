#  Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        else:
            combinations = []
            self.findCombinations(combinations, digits, 0, "")
            return combinations
        
    def findCombinations(self, combinations, digits, k, vect):
        if len(vect) == len(digits):
            combinations.append(vect)
        else:
            mapping = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
            
            for letter in mapping.get(int(digits[k])):
                w = vect + letter
                self.findCombinations(combinations, digits, k+1, w)
                
