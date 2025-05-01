#  https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # solution: 3D-DP
        # intuition: we compute the remainder for each path 

        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        MOD = 10**9 + 7

        for i in range(m):
            for j in range(n):
                for modulo in range(k):
                    left = dp[i][j-1][modulo] % MOD if j > 0 else 0
                    up = dp[i-1][j][modulo] % MOD if i > 0 else 0
                    dp[i][j][(modulo + grid[i][j]) % k] += left + up
        
        return dp[m-1][n-1][0] % MOD
