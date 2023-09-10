#  https://leetcode.com/problems/number-of-enclaves/description/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # solution: DFS

        # --- DFS on all 1s on the outside
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            grid[i][j] = 'X'
            visited.add((i,j))

            directions = [[1,0], [0,1], [-1,0], [0, -1]]
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n) and (grid[x][y] == 1) and (x,y) not in visited:
                    dfs(x,y)
     
        
        for j in range(n):
            if grid[0][j] == 1: dfs(0, j)
            if grid[m-1][j] == 1: dfs(m-1, j)
        
        for i in range(m):
            if grid[i][0] == 1: dfs(i, 0)
            if grid[i][n-1] == 1: dfs(i, n-1)

        # --- count remaining 1s inside the grid 
        remaining = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    remaining += 1
        
        return remaining
