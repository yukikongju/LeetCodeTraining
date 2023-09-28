#  https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # solution: bitmasking
        # a number is a power of two if it has only one '1' -> ex: 100000 ; 100

        # base case: if negative, has at least two ones bc one '-'
        if n <= 0: return False

        # --- count number of one with bitmasking
        num_ones = 0
        while n:
            bit = n & 1
            if bit: num_ones += 1
            n >>= 1
        
        return True if num_ones == 1 else False
        

