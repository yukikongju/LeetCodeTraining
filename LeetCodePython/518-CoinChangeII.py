#  https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Solution: DP Memoization
        m, n = len(coins), amount + 1

        # edge case: amount = 0
        if amount == 0:
            return 1

        # --- init dp table
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # --- fill table: (1) top (2) left: amount - domination (3) equal: amount == domination
        for i in range(m):
            for j in range(n):
                c1 = dp[i-1][j] if i-1 >= 0 else 0
                c2 = dp[i][j - coins[i]] if (j - coins[i] >= 0) else 0
                c3 = 1 if (j == coins[i]) else 0
                dp[i][j] = c1 + c2 + c3

        return dp[m-1][n-1]

        
