class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution: 2D DP
        # intuition: 2 states: buy or sell -> decision: perform the action or not 
        # 

        n = len(prices)
        if n == 1: return 0

        b = [float('-inf') for _ in range(n)]
        s = [0 for _ in range(n)]

        for i in range(n):
            s[i] = max(s[i-1], prices[i] + b[i-1])
            b[i] = max(b[i-1], s[i-2] - prices[i])
            
        return s[-1]

