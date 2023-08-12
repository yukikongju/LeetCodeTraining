#  https://leetcode.com/problems/longest-palindromic-subsequence/description/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # solution: 2D DP -> construct table where row is s and columns is s'
        n = len(s)
        t = s[::-1]

        # --- init
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        # --- fill table: 
        for i in range(1, n+1):
            for j in range(1, n+1):
                c1 = 1 + dp[i-1][j-1] if s[i-1] == t[j-1] else 0 # take diago
                c2 = max(dp[i-1][j], dp[i][j-1]) # max(top, left)
                dp[i][j] = max(c1, c2)
        
        # ---
        return dp[n][n]
