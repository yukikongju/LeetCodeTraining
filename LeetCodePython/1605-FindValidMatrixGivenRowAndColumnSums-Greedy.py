#  https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/solutions/876904/python-c-greedy-easy-python-solution-explained-using-images/

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # solution: greedy
        # we want to subsract the smallest value to the col
        # explanation: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/solutions/876904/python-c-greedy-easy-python-solution-explained-using-images/

        # ---
        m, n = len(rowSum), len(colSum)
        mat = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r, c = rowSum[i], colSum[j]
                min_val = min(r, c)
                mat[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
        # ---
        return mat
