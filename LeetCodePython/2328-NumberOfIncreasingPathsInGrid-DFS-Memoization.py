#  https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # solution: DFS + Memoization
        # for each cells, we find the length of the longest increasing path and sum them

        # ---
        m, n = len(grid), len(grid[0])
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        mod = 10**9 + 7

        # ---
        def dfs(i, j):
            if visited[i][j] != -1:
                return visited[i][j]

            longest_path_length = 1
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n) and (grid[i][j] < grid[x][y]):
                    longest_path_length += dfs(x,y)
            visited[i][j] = longest_path_length
            return longest_path_length

        # ---
        num_paths = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == -1:
                    visited[i][j] = dfs(i, j)
                num_paths = (num_paths + visited[i][j]) % mod

        # ---
        return num_paths


