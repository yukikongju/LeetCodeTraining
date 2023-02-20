class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Sol: binary search: 
        # (1) finding row: compare first and last value of row
        # (2) finding target inside row: classic binary search

        m, n = len(matrix), len(matrix[0])

        # find row where target is
        top, bottom = 0, m-1
        while top <= bottom: 
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row-1
            elif target > matrix[row][-1]:
                top = row+1
            else: 
                break

        row = (top + bottom) // 2


        # find target in the row
        left, right = 0, n-1
        while left <= right: 
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid -1
            else: 
                return True
        
        return False
