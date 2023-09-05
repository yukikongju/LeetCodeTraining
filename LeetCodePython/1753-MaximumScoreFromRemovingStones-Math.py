#  https://leetcode.com/problems/maximum-score-from-removing-stones/description/

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # solution: math
        # always take from largest and another one

        # --- find which a,b,c is max, min, middle
        maximum = max(a, b, c)
        minimum = min(a, b, c)
        middle = a + b + c - maximum - minimum
        
        # ---
        if maximum >= minimum + middle:
            return min(maximum, minimum + middle)
        else:
            tmp = minimum + middle
            res = maximum + (tmp-maximum) // 2
            return res


