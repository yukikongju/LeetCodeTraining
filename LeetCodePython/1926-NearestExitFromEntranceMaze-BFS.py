#  https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # solution: bfs

        # --- find all possible exits: check outside box and remove entrance 
        exits = set()
        m, n = len(maze), len(maze[0])
        entrance = tuple(entrance)

        for i in range(m):
            if maze[i][0] == '.':
                exits.add((i, 0))
            if maze[i][n-1] == '.':
                exits.add((i, n-1))
        
        for j in range(n):
            if maze[0][j] == '.':
                exits.add((0,j))
            if maze[m-1][j] == '.':
                exits.add((m-1,j))
        
        if entrance in exits:
            exits.remove(entrance)

        # --- perform bfs
        visited = set()
        queue = [(entrance, 0)] # position (i,j) ; num_steps

        while queue:
            pos, d = queue.pop(0)
            x, y = pos

            if (x,y) in exits:
                return d
            
            if (x,y) in visited:
                continue
            
            visited.add((x,y))
            directions = [(-1, 0), (1,0), (0,-1), (0,1)]
            for dx, dy in directions:
                row, col = x+dx, y+dy
                if (row>=0) and (row<m) and (col>=0) and (col<n) and ((row,col) not in visited) and maze[row][col] == '.':
                    queue.append(((row, col), d+1))

        # ---
        return -1




