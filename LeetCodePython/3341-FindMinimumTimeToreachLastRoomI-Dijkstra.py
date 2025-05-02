#  https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # solution: dijkstra

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(moveTime), len(moveTime[0])
        visited = [[False] * n for _ in range(m)]
        times = [[float('inf')] * n for _ in range(m)]

        visited[0][0] = True
        times[0][0] = 0

        pq = [(0, 0, 0)] # (time, i, j)
        while pq: 
            time, i, j = heapq.heappop(pq)
            if time > times[i][j]:
                continue
            
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    new_time = max(time, moveTime[x][y]) + 1
                    if new_time < times[x][y]:
                        times[x][y] = new_time
                        heapq.heappush(pq, (new_time, x, y))
        
        return times[-1][-1]
            


        
