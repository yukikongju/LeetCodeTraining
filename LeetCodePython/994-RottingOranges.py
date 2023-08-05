#  https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # solution: bfs
        m, n = len(grid), len(grid[0])

        # --- find rotten oranges
        stack = []
        num_fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append([i,j])
                elif grid[i][j] == 1:
                    num_fresh_oranges += 1
        
        # --- bfs to rot the oranges
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        num_minutes = 0
        while stack and num_fresh_oranges > 0:
            for _ in range(len(stack)):
                x, y = stack.pop(0)
                # check adjacent to determine if we rot it
                for dr, dc in directions:
                    row, col = x + dr, y + dc
                    if (row >= 0) and (row < m) and (col >= 0) and (col < n) and (grid[row][col] == 1):
                        grid[row][col] = 2
                        stack.append([row, col])
                        num_fresh_oranges -= 1
            num_minutes += 1


        # --- determine if it's possible or not: if there are still fresh oranges, then impossible
        return num_minutes if num_fresh_oranges == 0 else -1


