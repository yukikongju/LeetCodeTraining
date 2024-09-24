#  https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # solution: sliding  O(n)
        # idea: instead of removing from both ends, we try to find the
        #   maximum subarray length which sum sums to sum(nums) - 
        target = sum(nums) - x
        
        # - edge case
        if target < 0:
            return -1
        if target == 0:
            return len(nums) 

        #
        longest = 0
        left, right = 0, 0
        current_sum = 0
        while right < len(nums):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                longest = max(longest, right - left + 1)
            right += 1

        return -1 if longest == 0 else len(nums) - longest
