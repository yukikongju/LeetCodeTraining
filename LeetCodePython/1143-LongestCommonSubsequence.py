#  https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # solution: 2D DP
        m, n = len(text1), len(text2)

        # --- init
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # --- solve dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                c1 = 1 + dp[i-1][j-1] if (text1[i-1] == text2[j-1]) else 0 
                c2 = max(dp[i-1][j], dp[i][j-1])
                dp[i][j] = max(c1, c2)
        
        # --- 
        return dp[m][n]
        
