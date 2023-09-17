#  https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        # solution: Maths
        if n == 0:
            return 0
        
        # ---
        for i in [2,3,5]:
            while (n%i==0):
                n /= i
        
        return n == 1
