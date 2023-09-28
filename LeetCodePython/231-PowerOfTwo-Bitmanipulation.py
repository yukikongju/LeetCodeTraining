#  https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # solution: bit manipulation - O(1)
        # n&(n-1) == 0 => 1000 & 0111 == 0

        # base case: 
        if n <= 0: return False

        return n & (n-1) == 0
        
