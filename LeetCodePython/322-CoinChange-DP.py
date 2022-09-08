#  Link: https://leetcode.com/problems/coin-change/

# Similar to : 983. Minimum Cost for Tickets
# Reformulation: 


#  Time Complexity: O(n^2)

#  Follow-up: (1) Which coins are you giving? (2) What if the number of coins 
#  are finite? (3) 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Solution: DP => dp[i][j] = min(dp[i-1][j], dp[i][j - coins[i-1]] + 1) 
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins))]
        
        for i in range(len(coins)):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 0
                elif j-coins[i] >= 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
                else: 
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

