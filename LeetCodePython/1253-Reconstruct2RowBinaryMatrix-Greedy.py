#  https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        # solution: greedy

        # ---
        n = len(colsum)
        upper_row = [0 for _ in range(n)]
        lower_row = [0 for _ in range(n)]

        for i, val in enumerate(colsum):
            if (val == 1): # do we add upper or lower
                if upper > lower:
                    upper_row[i] = 1
                    upper -=1
                else:
                    lower_row[i] = 1
                    lower -= 1
            elif (val == 2): 
                upper_row[i] = lower_row[i] = 1
                upper -= 1
                lower -= 1
        
        return [upper_row, lower_row] if upper == lower == 0 else []



