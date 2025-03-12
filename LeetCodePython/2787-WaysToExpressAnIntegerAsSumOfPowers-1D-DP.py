#  https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # solution: 1D DP 
        # intuition: generate possible values to use for the sum -> turn the problem into number combinations 
        # in sorted order
        # dp => how many ways to make values

        MOD = 10**9 + 7
        dp = [0] * (n+1)
        dp[0] = 1

        for num in range(1, n+1):
            m = num**x
            for j in range(n, 0, -1):
                if j - m >= 0:
                    dp[j] += dp[j - m]
                    dp[j] %= MOD
        
        return dp[-1] % MOD

