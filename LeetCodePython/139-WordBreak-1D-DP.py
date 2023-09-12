#  https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        # solution: 1D DP
        m = len(s)
        dp = [False for _ in range(m)]


        for i in range(m):
            for word in words:
                n = len(word)
                if i < n-1:
                    continue
                if word == s[i-n+1: i+1]:
                    prev = dp[i-n] if i-n>=0 else True
                    dp[i] = prev or dp[i]

        
        return dp[m-1]
        
