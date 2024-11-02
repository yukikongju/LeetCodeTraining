#  https://leetcode.com/problems/maximum-width-ramp/description/
# Time Limit Exceeded
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # solution: hashmap => O(n^2)
        # ex: [6,0,8,2,1,5] => positions: [-1, -1, 0, 1, 1, 1]

        # remember position of the furtest
        n = len(nums)
        positions = [-1 for _ in range(n)]
        for i, num in enumerate(nums):
            for j in range(i, n):
                if nums[i] <= nums[j] and positions[j] == -1:
                    positions[j] = i
        
        # compute largest width
        largest = 0 
        for i in range(n):
            largest = max(largest, i - positions[i])

        return largest
