#  https://leetcode.com/problems/count-vowels-permutation/description/
#  https://www.youtube.com/watch?v=VUVpTZVa7Ls&t=564s

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # solution: DP => which character can be followed by <letter>?

        # initialize dp
        a, e, i, o, u = 0, 1, 2, 3, 4 # indices
        dp = [[0 for _ in range(n)] for _ in range(5)]
        for j in range(5):
            dp[j][0] = 1
        
        modulo = 10**9 + 7

        # DP
        for j in range(1, n):
            dp[a][j] = (dp[e][j-1] + dp[i][j-1] + dp[u][j-1]) % modulo
            dp[e][j] = (dp[a][j-1] + dp[i][j-1]) % modulo
            dp[i][j] = (dp[e][j-1] + dp[o][j-1]) % modulo
            dp[o][j] = dp[i][j-1]
            dp[u][j] = (dp[i][j-1] + dp[o][j-1]) % modulo
        
        #
        num_values = (dp[a][n-1] + dp[e][n-1] + dp[i][n-1] + dp[o][n-1] + dp[u][n-1]) % modulo
        return num_values





