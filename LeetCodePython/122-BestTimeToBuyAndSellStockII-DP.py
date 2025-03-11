#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1570373147/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution: DP
        # intuition:

        n = len(prices)
        if n == 1: return 0

        b = [float('-inf')] * n
        s = [0] * n
        for i in range(n):
            s[i] = max(s[i-1], b[i-1] + prices[i]) # not sell or sell
            b[i] = max(b[i-1], s[i-1] - prices[i]) # hold or sell
        
        return s[-1]
