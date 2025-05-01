#  https://leetcode.com/problems/find-a-safe-walk-through-a-grid/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # solution: BFS

        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        m, n = len(grid), len(grid[0])

        visited = [[-1] * n for _ in range(m)]
        queue = deque([(0, 0, health - grid[0][0])]) # (i, j, health)
        visited[0][0] = health - grid[0][0]
        while queue:
            i, j, health = queue.popleft()

            if health <= 0:
                continue
            if i == m-1 and j == n-1 and health > 0:
                return True

            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and health - grid[x][y] > 0:
                    new_health = health - grid[x][y]
                    if new_health > visited[x][y]:
                        visited[x][y] = new_health
                        queue.append((x, y, new_health))

        return False

