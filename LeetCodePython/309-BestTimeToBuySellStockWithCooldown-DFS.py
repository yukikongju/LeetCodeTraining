#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution: DFS with caching -> 
        # two states:
        # (1) buying state: we can buy or cooldown 
        # (2) selling state: we can sell or cooldown 

        dp = {}

        def dfs(i, can_buy: bool):
            if i >= len(prices): # if outside
                return 0
            if (i, can_buy) in dp: # if already in cache
                return dp[(i, can_buy)]
            
            if can_buy: 
                buy = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, True)
                dp[(i, can_buy)] = max(buy, cooldown)
            else: 
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, False)
                dp[(i, can_buy)] = max(sell, cooldown)
            
            return dp[(i, can_buy)]
        
        return dfs(0, True)
            
        
