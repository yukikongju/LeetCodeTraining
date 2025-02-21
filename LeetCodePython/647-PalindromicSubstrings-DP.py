#  https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        # solution: 2D DP - expanding from middle using i and j as index slicers
        # intuition: dp[i][j] determines if it's a palindrome or not
        # for even:
        # for odd:

        count = 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for j in range(n):
            for i in range(j):
                if s[i] == s[j] and (dp[i+1][j-1] or i+1 == j):
                    dp[i][j] = True
                    count += 1
        
        return count

