#  https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # solution: bitmasking

        num_ones = 0
        while n:
            bit = n & 1
            if bit: num_ones += 1
            n >>= 1

        return num_ones
        
