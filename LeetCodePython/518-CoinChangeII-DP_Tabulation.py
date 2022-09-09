#  Link: https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP Tabulation:
        # DP: dp[i][j] = dp[i-1][j] + dp[i][j - coins[i]]
        
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        
        # initialize tablulation
        for i in range(len(coins)): 
            dp[i][0] = 1
        
        # fill tableau
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j-coins[i] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i]]
                else: 
                    dp[i][j] = dp[i-1][j]
                    
        
        return dp[-1][-1]

