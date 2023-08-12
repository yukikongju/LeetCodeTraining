#  https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Solution: 2D DP -> next letter either come from s1 or s2
        m, n = len(s1), len(s2)

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True

        # base case:
        if len(s1) + len(s2) != len(s3):
            return False

        # ---
        for i in range(0, m+1):
            for j in range(0, n+1):
                if i == 0 and j == 0: 
                    continue
                c1 = True if (dp[i-1][j] == True) and (s1[i-1] == s3[i+j-1]) else False
                c2 = True if (dp[i][j-1] == True) and (s2[j-1] == s3[i+j-1]) else False
                dp[i][j] = c1 or c2


        return dp[m][n]

