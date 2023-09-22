#  https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # solution: Hard sliding window

        # ---
        current_sum = sum(nums[:k])
        max_average = current_sum / k
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            average = current_sum / k
            max_average = max(max_average, average)

        return max_average            

        
