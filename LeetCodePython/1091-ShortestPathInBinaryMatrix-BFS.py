#  https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # solution: BFS
        n = len(grid)

        # base case
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # bfs
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        queue = deque([(0, 0, 1)]) # (i, j, distance)
        while queue:
            i, j, d = queue.popleft()
            if i == n-1 and j == n-1:
                return d
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 0 and not visited[x][y]:
                    visited[x][y] = True
                    queue.append([x, y, d+1])
        return -1
            


        
