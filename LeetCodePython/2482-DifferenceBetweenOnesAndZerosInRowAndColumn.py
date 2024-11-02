#  https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # sol: count dict

        # compute sums for each row/col
        m, n = len(grid), len(grid[0])
        onesRow = [sum(grid[i]) for i in range(m)]
        zerosRow = [n - onesRow[i] for i in range(m)]
        onesCol = [sum(grid[j][i] for j in range(m)) for i in range(n)]
        zerosCol = [m - onesCol[i] for i in range(n)]

        # compute 
        out = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                out[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        return out
