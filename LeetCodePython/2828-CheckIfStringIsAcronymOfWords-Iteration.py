#  https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # solution: iteration
        t = ""
        for word in words:
            t += word[0]
        
        return t == s
        
