#  Link: https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        
    def solve(self):
        # 1. find cell to fill
        row, col = self.find_empty_cell()
        if row == -1 and col == -1:
            return True
        else:
            # 2. test value in cell
            for val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if self.is_safe(val, row, col):
                    self.board[row][col] = val
                    if self.solve():
                        return True
                    self.board[row][col] = "."
            return False
    
    def is_safe(self, val, row, col):
        # Sol: check if value can be put in cell: (1) row (2) col (3) square
        return self.check_row(val, row, col) and self.check_col(val, row, col) and self.check_square(val, row, col)
            
    def check_row(self, val, row, col):
        for k in range(len(self.board[0])):
            if self.board[row][k] == val:
                return False
        return True
    
    def check_col(self, val, row, col):
        for k in range(len(self.board)):
            if self.board[k][col] == val:
                return False
        return True
    
    def check_square(self, val, row, col):
        box_row = row - row % 3
        box_col = col - col % 3
        for i in range(box_row, box_row+3):
            for j in range(box_col, box_col+3):
                if self.board[i][j] == val:
                    return False
        return True
            
    def find_empty_cell(self):
        # return row, col ; -1, -1 if board is full
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == ".":
                    return i, j
        return -1, -1
