#  https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n: int) -> int:
        # solution: 1D-DP

        # --- base case
        if n == 1:
            return 1
        
        # 1. find all squares up to n
        squares = []
        square , i = 1, 1 
        while square <= n:
            squares.append(square)
            square = i**2
            i += 1
        
        # 2. construct 1D dp: 
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            for num in squares:
                if i - num >= 0:
                    dp[i] = min(dp[i], dp[i-num]+1)

        return dp[n]
