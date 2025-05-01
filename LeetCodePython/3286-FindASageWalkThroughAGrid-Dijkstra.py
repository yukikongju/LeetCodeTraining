#  https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # solution: dijkstra

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(grid), len(grid[0])
        distances = [[float('inf')] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        pq = [(0, 0, grid[0][0])]
        heapq.heapify(pq)

        visited[0][0] = True
        distances[0][0] = grid[0][0]

        while pq:
            i, j, dist = heapq.heappop(pq)
            visited[i][j] = True

            if dist > distances[i][j]:
                continue
            
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and dist + grid[x][y] < distances[x][y]:
                    distances[x][y] = dist + grid[x][y]
                    visited[x][y] = True
                    heapq.heappush(pq, (x, y, distances[x][y]))
        
        return distances[-1][-1] < health 
        
