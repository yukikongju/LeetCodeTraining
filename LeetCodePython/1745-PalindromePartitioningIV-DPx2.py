#  https://leetcode.com/problems/palindrome-partitioning-iv/

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # solution: DP + Backtracking
        # intuition: 
        # 1. compute palindromic subsequences with DP - expand from middle
        # 2. Backtrack to generate partition

        # --- compute palindromic subsequences
        res = []
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for j in range(n):
            for i in range(j):
                if (s[i] == s[j]) and (dp[i+1][j-1] or i+1 == j):
                    dp[i][j] = True

        # --- find valid 3-length partitions with DP - if one string is a prefix and another one is 
        # a suffix, then we can brute-force the rest
        for i in range(n):
            for j in range(i):
                if dp[0][j] and dp[j+1][i-1] and dp[i][n-1]:
                    return True
        return False
        
