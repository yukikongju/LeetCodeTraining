#  Link: https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Sol: pointers
        
        if len(matrix) == 0:
            return []
        
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n -1
        order = []
        
        
        
        # add 
        while left <= right and top <= bottom:
            # left to right
            for k in range(left, right+1):
                order.append(matrix[top][k])
            top += 1
            
            # top to bottom
            for k in range(top, bottom+1):
                order.append(matrix[k][right])
            right -= 1
                
            # right to left
            for k in range(right, left-1, -1):
                order.append(matrix[bottom][k])
            bottom -= 1
                
            # bottom to top
            for k in range(bottom, top-1, -1):
                order.append(matrix[k][left])
            left += 1
        
        # edge case: ignore redundant         
        return order[:m*n]
                
        
