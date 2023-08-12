#  https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # solution: 2D DP
        m, n = len(grid), len(grid[0])

        # --- init 
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[0][0] = grid[0][0]

        # --- fill table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[0][j] = dp[0][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][j] + grid[i][j]
                else:
                    top = dp[i-1][j]
                    left = dp[i][j-1]
                    dp[i][j] = min(top, left) + grid[i][j]         
        
        # ---
        return dp[m-1][n-1]

