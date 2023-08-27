#  https://leetcode.com/problems/find-the-safest-path-in-a-grid/description/

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # solution: BFS + minHeap

        # --- base: 
        m, n = len(grid), len(grid[0])
        if (grid[0][0] == 1) or (grid[m-1][n-1] == 1):
            return 0

        # --- find all thieves positions
        thieves = [] # (i,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append((i, j))
        
        # --- find each cell distances to thief with BFS
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        distances = [[0 for _ in range(n)] for _ in range(m)]
        queue = [(0, i, j) for i,j in thieves]
        while len(visited) < m*n:
            dist, i, j = queue.pop(0)

            if (i,j) in visited:
                continue
            visited.add((i,j))
            distances[i][j] = dist

            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n) and (x,y) not in visited:
                    queue.append((dist+1, x, y))

        # --- find safeness factor with MaxHeap // Dijkstra
        visited = set()
        minHeap = [(-distances[0][0], 0, 0)] # (dist, i, j)
        max_safeness = 0

        while minHeap:
            safeness, i, j = heapq.heappop(minHeap)

            if (i,j) in visited:
                continue
            visited.add((i,j))

            if (i==m-1) and (j==n-1):
                return -safeness


            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n) and (x,y) not in visited:
                    next_safeness = max(safeness, -distances[x][y])
                    heapq.heappush(minHeap, (next_safeness, x, y))



        # ---
