#  Link: https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Sol
        m, n = len(board), len(board[0])
        self.found = False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [(i,j)]
                    self.findWord(board, word, visited, 0, i, j)
        
        return self.found
    
    def findWord(self, board, word, visited, k, i, j): # i: row, j: col
        # DFS: (1) neighbor exist, (2) hasn't been visited yet (3) neighbor is word[k+1]
        if k == len(word)-1:
            self.found = True
        elif not self.found:
            next_letter = word[k+1]
            # top
            if (i-1>=0) and ((i-1, j) not in visited) and (board[i-1][j] == next_letter):
                w_visited = visited + [(i-1, j)] 
                self.findWord(board, word, w_visited, k+1, i-1, j)
            
            # right
            if (j+1<len(board[0])) and ((i, j+1) not in visited) and (board[i][j+1] == next_letter):
                w_visited = visited + [(i, j+1)] 
                self.findWord(board, word, w_visited, k+1, i, j+1)
            
            # left
            if (j-1>=0) and ((i, j-1) not in visited) and (board[i][j-1] == next_letter):
                w_visited = visited + [(i, j-1)] 
                self.findWord(board, word, w_visited, k+1, i, j-1)
            
            # bottom
            if (i+1<len(board)) and ((i+1, j) not in visited) and (board[i+1][j] == next_letter):
                w_visited = visited + [(i+1, j)] 
                self.findWord(board, word, w_visited, k+1, i+1, j)
            
        
            
