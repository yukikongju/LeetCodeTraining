#  https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # solution: DP
        # same solution as Pascal Triangle I, but we only return last element of output

        prev = [1]
        output = [prev]

        if rowIndex == 0:
            return [1]

        for i in range(rowIndex+1):
            row = [1]
            j=1

            while(j<i):
                row.append(prev[j-1] + prev[j])
                j+=1
            row.append(1)
            output.append(row)
            prev = row
        
        return output[-1]
