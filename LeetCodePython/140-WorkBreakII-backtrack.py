#  https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # solution: backtracking

        solutions = []
        n = len(s)

        def backtracking(i, words):
            if i > n:
                return
            if i == n:
                solutions.append(" ".join(words))
            for word in wordDict:
                m = len(word)
                if word == s[i: i+m]:
                    backtracking(i+m, words + [word])
            
        
        backtracking(0, [])
        return solutions
