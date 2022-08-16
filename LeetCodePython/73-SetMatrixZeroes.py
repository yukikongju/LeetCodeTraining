#  Link: https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Sol: traverse and flag if not 0
        
        # first pass: flag
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.flag(matrix, i, j)
        
        # second pass: unflag
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '.':     # unflag if flagged
                    matrix[i][j] = 0
        
        return matrix
        
        
    def flag(self, matrix, row, col):
        m, n = len(matrix), len(matrix[0])
        
        # flag row
        for k in range(n):
            if matrix[row][k] != 0:
                matrix[row][k] = '.'
        
        # flag column
        for k in range(m):
            if matrix[k][col] != 0:
                matrix[k][col] ='.'
    
        
        
