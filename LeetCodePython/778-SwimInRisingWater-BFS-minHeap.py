class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # solution: BFS + minHeap

        # ---
        m, n = len(grid), len(grid[0])
        minHeap = [(grid[0][0], 0, 0)] # (val, i, j)
        visited = set((0, 0)) # (i,j)

        # ---
        while minHeap:
            val, i, j = heapq.heappop(minHeap)

            # check if we have reached goal
            if (i == m-1) and (j == n-1):
                return val

            # find next steps
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n) and ((x,y) not in visited):
                    dist = max(grid[x][y], val)
                    heapq.heappush(minHeap, (dist, x, y))
                    visited.add((x,y))



