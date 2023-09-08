#  https://leetcode.com/problems/battleships-in-a-board/description/

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # solution: DFS

        # ---
        count = 0
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        def dfs(i, j):
            board[i][j] = '0'
            visited.add((i, j))

            for dx, dy in directions:
                x, y = i+dx, j+dy
                if (x>=0) and (x<m) and (y>=0) and (y<n) and board[x][y] == 'X' and ((x,y) not in visited):
                    dfs(x,y)
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    count += 1
                    dfs(i, j)
        
        return count
