#  https://leetcode.com/problems/valid-sudoku/
# Neetcode

def isValidSudoku(board):
    m, n = len(board), len(board[0])

    # 1. check if rows are valid
    for i in range(m):
        row = board[i]
        if not isValid(row):
            return False

    # 2. check if columns are valid
    for j in range(n):
        col = [board[i][j] for i in range(m)]
        if not isValid(col):
            return False

    # 3. check if squares are valid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not isValid(square):
                return False

    return True

def isValid(cells):
    """ 
    cells: list of values in row/col/cells
    """
    values = [cell for cell in cells if cell != '.']
    return len(values) == len(set(values))
    

def test1():
    board = [
            ["5","3",".",".","7",".",".",".","."] ,
            ["6",".",".","1","9","5",".",".","."] ,
            [".","9","8",".",".",".",".","6","."] ,
            ["8",".",".",".","6",".",".",".","3"] ,
            ["4",".",".","8",".","3",".",".","1"] ,
            ["7",".",".",".","2",".",".",".","6"] ,
            [".","6",".",".",".",".","2","8","."] ,
            [".",".",".","4","1","9",".",".","5"] ,
            [".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board) == True)

def test2():
    board = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board) == False)


def main():
    test1()
    test2()
    

if __name__ == "__main__":
    main()
