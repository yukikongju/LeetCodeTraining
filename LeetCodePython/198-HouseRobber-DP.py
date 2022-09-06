class Solution:
    def rob(self, nums: List[int]) -> int:
        # T[i] = max(nums[i] + T[i-2], T[i-1]) => on rob ou on rob pas
        # base case: dp[0] = nums[0]; dp[1] = max(nums[0], nums[1])
        # step: dp[k] = max(nums[k] + dp[k-2], dp[k-1])
        
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else: 
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]
        
        
