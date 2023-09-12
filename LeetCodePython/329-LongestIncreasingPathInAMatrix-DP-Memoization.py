#  https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # solution: DP + DFS

        # ---
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            nonlocal longest_path

            if (dp[i][j] != 0): return dp[i][j]

            directions = [[1,0], [-1,0], [0,-1], [0,1]]
            max_path_length = 1
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n) and matrix[i][j] < matrix[x][y]:
                    dfs(x,y)
                    max_path_length = max(max_path_length, dp[x][y] + 1)
            dp[i][j] = max_path_length
            return max_path_length

        # --- 
        for i in range(m):
            for j in range(n):
                dfs(i,j)

        print(dp)

        # --- find longest path
        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dp[i][j])

        return longest_path
