#  https://leetcode.com/problems/find-triangular-sum-of-an-array/description/

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # solution: DP

        output = []
        n = len(nums)

        if n == 1:
            return nums[0]

        for i in range(n):
            if (i==0):
                output.append(nums)
            else:
                row = []
                prev = output[-1]
                j=1
                while (j<n-i+1):
                    val = (prev[j-1]+prev[j]) % 10 
                    row.append(val)
                    j+=1 
                # print(row)
                output.append(row)
        
        return output[-1][0]

