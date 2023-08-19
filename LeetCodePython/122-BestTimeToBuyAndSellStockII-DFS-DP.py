#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution: DFS + caching

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
                sell = dfs(i+1, True) + prices[i]
                hold = dfs(i+1, False)
                dp[(i, can_buy)] = max(sell, hold)
            
            return dp[(i, can_buy)]
        
        return dfs(0, True)

        


