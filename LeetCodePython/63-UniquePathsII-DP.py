#  https://leetcode.com/problems/unique-paths-ii/description/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # solution: 2D DP
        # init: first row/col = 1
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # ---
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[0][0] = 1

        # ---
        for i in range(m):
            for j in range(n):
                if (i==0) and (j==0): # init: dp[0][0] = 1
                    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
                elif (obstacleGrid[i][j] == 0):
                    top = dp[i-1][j] if i-1>=0 else 0 
                    left = dp[i][j-1] if j-1>=0 else 0
                    dp[i][j] = top + left

        # ---
        return dp[m-1][n-1]

