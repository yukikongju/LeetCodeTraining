#  https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/description/

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # solution: math O(n)

        max_num_pens = total // cost1
        res = 0
        for num_pen in range(max_num_pens + 1):
            res += (total - num_pen * cost1) // cost2 + 1
        return res
        
