#  Link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Sol: DFS + flag visited cell
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        
        return count
    
    def dfs(self, grid, i, j):
        # mark cell + call dfs on neighbor if (1) neighbor is valid and (2) it is "1" 
        grid[i][j] = "X"
        
        # top
        if (i-1>=0) and (grid[i-1][j] == "1"):
            self.dfs(grid, i-1, j)
            
        # bottom
        if (i+1<len(grid)) and (grid[i+1][j] == "1"):
            self.dfs(grid, i+1, j)
        
        # left
        if (j-1>=0) and (grid[i][j-1] == "1"):
            self.dfs(grid, i, j-1)
        
        # right
        if (j+1<len(grid[0])) and (grid[i][j+1] == "1"):
            self.dfs(grid, i, j+1)
            
            
