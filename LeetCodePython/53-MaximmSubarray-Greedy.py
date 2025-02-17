class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # solution: greedy => if the current sum is negative, then we don't use the subarray 
        # to build our sum

        largest = current = nums[0]
        for i in range(1, len(nums)):
            if current < 0:
                current = 0
            
            current += nums[i]
            largest = max(largest, current)
        return largest
