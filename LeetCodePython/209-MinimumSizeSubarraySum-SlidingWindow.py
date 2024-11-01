#  https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Solution: Sliding Window O(n)

        min_length = float('inf')
        start = 0
        current_sum = 0
        for end, num in enumerate(nums):
            current_sum += num
            if current_sum >= target:
                while (start+1 <= end) and (current_sum - nums[start] >= target):
                    current_sum -= nums[start]
                    start += 1
                min_length = min(min_length, end-start+1)

        return 0 if min_length == float('inf') else min_length
