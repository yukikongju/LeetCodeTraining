#  https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Solution: DP

        output = []

        for i in range(numRows):
            if (i == 0):
                prev = [1]
                output.append(prev)
            else:
                row = [1]
                j = 1

                while (j<i):
                    row.append(prev[j-1] + prev[j])
                    j+=1
                row.append(1)
                output.append(row)
                prev = row

        return output
        
