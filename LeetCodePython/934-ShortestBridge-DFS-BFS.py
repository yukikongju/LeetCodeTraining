#  https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Solution: DFS to find islands; BFS to find distances
        # intuition: 
        # 1. DFS => get the first island from the first cell 
        # 2. BFS => from all spot if first island, try to reach the 2nd one
        # note: we can't use a heap because it keeps old solution

        m, n = len(grid), len(grid[0])
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        # --- DFS
        start = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == 1)
        stack = [(start[0], start[1])]
        visited = set(stack) 
        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited:
                    stack.append((x, y))
                    visited.add((x, y))
        
        # --- BFS - Level Order
        ans = 0
        queue = list(visited)
        while queue:
            new_queue = []
            for i, j in queue:
                for dx, dy in directions:
                    x, y = i+dx, j+dy
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                        if grid[x][y] == 1:
                            return ans
                        new_queue.append((x, y))
                        visited.add((x, y))
            queue = new_queue
            ans += 1
            
        return ans
