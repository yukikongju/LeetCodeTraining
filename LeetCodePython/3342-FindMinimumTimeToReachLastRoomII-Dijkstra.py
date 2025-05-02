#  https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description/

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # solution: dijkstra

        m, n = len(moveTime), len(moveTime[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        distances = [[float('inf')] * n for _ in range(m)]
        distances[0][0] = 0

        pq = [(0, 0, 0, 1)] # (dist, i, j, step_cost)
        while pq:
            dist, i, j, step_cost = heapq.heappop(pq)

            if i == m-1 and j == n-1:
                return dist

            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n:
                    d = 1 if step_cost == 1 else 2
                    wait_time = max(moveTime[x][y] - dist, 0)
                    new_dist = dist + d + wait_time
                    if new_dist < distances[x][y]:
                        next_step_cost = 2 if step_cost == 1 else 1
                        distances[x][y] = new_dist
                        heapq.heappush(pq, (distances[x][y], x, y, next_step_cost))
        
        return -1
        
