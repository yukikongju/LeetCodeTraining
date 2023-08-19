#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # solution: DFS with cache

        # ---
        dp = {} # (pos, can_buy)

        def dfs(i, can_buy):
            if (i==len(prices)):
                return 0
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]
            
            #
            if can_buy:
                buy = dfs(i+1, False) - prices[i]
                hold = dfs(i+1, True)
                dp[(i, can_buy)] = max(buy, hold)
            else:
                sell = dfs(i+1, True) + prices[i] - fee
                hold = dfs(i+1, False)
                dp[(i, can_buy)] = max(sell, hold)
            
            return dp[(i, can_buy)]
        
        # ---
        return dfs(0, True)
