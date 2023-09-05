#  https://leetcode.com/problems/maximum-ice-cream-bars/description/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # solution: greedy
        # we buy the least expensive ice cream bars until we run out of money

        # --- sort
        costs.sort()

        # --- buy until we run out of money
        bars = 0
        while coins > 0 and costs:
            c = costs.pop(0)
            coins -= c
            if coins >= 0:
                bars += 1
        
        return bars
        
        
