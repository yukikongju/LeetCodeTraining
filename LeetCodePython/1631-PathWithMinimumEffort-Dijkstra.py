class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # solution: Dijkstra (with MinHeap)

        # ---
        m, n = len(heights), len(heights[0])
        minHeap = [(0, 0, 0)] # (min_distance, i, j)
        distances = [[float('inf') for _ in range(n)] for _ in range(m)]
            
        # ---
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while minHeap:
            effort, i, j = heapq.heappop(minHeap)
            if effort > distances[i][j]: continue
            if (i==m-1) and (j==n-1):
                return effort

            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n):
                    new_effort = max(effort, abs(heights[i][j] - heights[x][y]))
                    if new_effort < distances[x][y]:
                        distances[x][y] = new_effort
                        heapq.heappush(minHeap, (new_effort, x, y))



