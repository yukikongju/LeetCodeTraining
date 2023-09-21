#  https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # solution: sliding window

        # ---
        current_length = 0
        num_subarrays = 0
        for i, num in enumerate(nums):
            if num == 0:
                current_length += 1
                num_subarrays += current_length
            else:
                current_length = 0

        # ---
        return num_subarrays
