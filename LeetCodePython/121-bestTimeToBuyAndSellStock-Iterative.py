class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sol: iterate through price and update max profit and cheapest stock
        
        max_profit, lowest = 0, prices[0]
        for price in prices: 
            max_profit = max(max_profit, price - lowest)
            lowest = min(lowest, price)
        
        return max_profit
            
            
