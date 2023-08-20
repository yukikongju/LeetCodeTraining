#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # solution: DFS + DP
        # increment num_transactions only when selling

        dp = {}

        def dfs(i, can_buy, num_transactions):
            if (i==len(prices)) or num_transactions == k:
                return 0
            if (i, can_buy, num_transactions) in dp:
                return dp[(i, can_buy, num_transactions)]
            
            if can_buy:
                buy = dfs(i+1, False, num_transactions) - prices[i]
                hold = dfs(i+1, can_buy, num_transactions)
                dp[(i, can_buy, num_transactions)] = max(buy, hold)
            else:
                sell = dfs(i+1, True, num_transactions+1) + prices[i]
                hold = dfs(i+1, can_buy, num_transactions)
                dp[(i, can_buy, num_transactions)] = max(sell, hold)
            
            return dp[(i, can_buy, num_transactions)]
        
        return dfs(0, True, 0)

