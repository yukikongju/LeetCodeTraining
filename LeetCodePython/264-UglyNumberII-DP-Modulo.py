#  https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # solution: Maths + DP 
        # un multiple d'un ugly number is an ugly number

        # ---
        dp = [0 for _ in range(n)]
        dp[0] = 1
        a, b, c = 0, 0, 0

        for num in range(1, n):
            dp[num] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if (dp[a] * 2 == dp[num]): a += 1
            if (dp[b] * 3 == dp[num]): b += 1
            if (dp[c] * 5 == dp[num]): c += 1
        
        return dp[n-1]
