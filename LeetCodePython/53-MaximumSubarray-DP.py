class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP: we store the current max contiguous subarray
        
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[0]
            else:
                dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
 
        
