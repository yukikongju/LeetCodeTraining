#  https://leetcode.com/problems/maximum-width-ramp/description/
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # solution: Sliding Window
        # intuition: keep track of maximum values at the right of the indices

        # compute maximum values to the right
        max_right_values = []
        n = len(nums)
        max_val = nums[-1]
        for i in reversed(range(n)):
            max_val = max(max_val, nums[i])
            max_right_values.append(max_val)
        max_right_values = max_right_values[::-1]

        # sliding window to find the maximum width => O(n)
        max_width = 0
        left = 0
        for right in range(n):
            while nums[left] > max_right_values[right]:
                left += 1
            max_width = max(max_width, right - left)
        
        return max_width
