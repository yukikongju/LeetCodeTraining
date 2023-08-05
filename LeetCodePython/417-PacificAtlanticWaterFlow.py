#  https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Solution: determine which cells can reach pacific/atlantic and then do the intersection 
        m, n = len(heights), len(heights[0])

        # --- pacific ocean dfs
        can_reach_pacific = [[False for _ in range(n)] for _ in range(m)]
        left_queue_pacific = [[i,0] for i in range(m)]
        top_queue_pacific = [[0, j] for j in range(n)]
        queue_pacific = left_queue_pacific + top_queue_pacific
        visited_pacific = [[False for _ in range(n)] for _ in range(m)]

        directions = [[1, 0], [-1, 0], [0,-1], [0, 1]]
        while queue_pacific:
            row, col = queue_pacific.pop(0)
            visited_pacific[row][col] = True
            for x, y in directions: 
                neighbor_x, neighbor_y = row + x, col + y
                if (neighbor_x >= 0) and (neighbor_x < m) and (neighbor_y >= 0) and (neighbor_y < n) and (not visited_pacific[neighbor_x][neighbor_y]) and (heights[neighbor_x][neighbor_y] >= heights[row][col]):
                    queue_pacific.append([neighbor_x, neighbor_y])

        # --- atlantic ocean dfs
        can_reach_atlantic = [[False for _ in range(n)] for _ in range(m)]
        right_atlantic = [[i, n-1] for i in range(m)]
        bottom_atlantic = [[m-1, j] for j in range(n)]
        queue_atlantic = right_atlantic + bottom_atlantic
        visited_atlantic = [[False for _ in range(n)] for _ in range(m)]

        while queue_atlantic:
            row, col = queue_atlantic.pop(0)
            visited_atlantic[row][col] = True
            for x, y in directions:
                neighbor_x, neighbor_y = row + x, col + y
                if (neighbor_x >= 0) and (neighbor_x < m) and (neighbor_y >= 0) and (neighbor_y < n) and (not visited_atlantic[neighbor_x][neighbor_y]) and (heights[neighbor_x][neighbor_y] >= heights[row][col]):
                    queue_atlantic.append([neighbor_x, neighbor_y])

        # --- get intersection
        results = []
        for i in range(m):
            for j in range(n):
                if visited_pacific[i][j] and visited_atlantic[i][j]:
                    results.append([i, j])
        
        return results
        
