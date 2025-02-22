#  https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        # solution: DP x2
        # intuition: use DP to compute all palindrome and DP to compute minimum cuts

        # --- find all palindrome using DP - expand from the middle
        res = []
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for j in range(n):
            for i in range(j):
                if (s[i] == s[j]) and (dp[i+1][j-1] or i+1 == j):
                    dp[i][j] = True
        
        # --- find minimum cuts using DP
        cuts = [i for i in range(n)] # worse case: we need to partition every position
        for j in range(n):
            if dp[0][j]:    # if s[0:j+1], no cuts needed
                cuts[j] = 0
            else:
                for i in range(j):
                    if dp[i+1][j]:
                        cuts[j] = min(cuts[j], cuts[i] + 1)
        return cuts[-1]
        
