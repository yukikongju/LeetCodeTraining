#  https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # solution: Sliding Window

        # --- base case
        if len(prices) == 1:
            return 1

        # ---
        num_periods = 1
        current_descent = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] -1:
                current_descent += 1
                num_periods += current_descent
            else:
                current_descent = 1
                num_periods += current_descent

        # ---
        return num_periods
        

