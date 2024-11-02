#  https://leetcode.com/problems/01-matrix/description/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # solution: DFS

        # loop through all cells position with 0
        m, n = len(mat), len(mat[0])
        out = [[-1 for _ in range(n)] for _ in range(m)]
        q = [] # (i, j, dist)
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    out[i][j] == 0
                    visited[i][j] = True

        # fill in with distance
        while q:
            i, j, dist = q.pop(0)
            out[i][j] = dist

            # add neighbor if not visited yet 
            neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for dx, dy in neighbors:
                x, y = i+dx, j+dy
                if (x >=0) and (x < m) and (y >=0) and (y < n) and not visited[x][y]:
                    q.append((x, y, dist+1))
                    visited[x][y] = True
        
        return out
            


        
