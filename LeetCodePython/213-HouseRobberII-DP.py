class Solution:
    def rob(self, nums: List[int]) -> int:
        # since the house are in a circle, we cannot rob the house at both extremities. 
        # We need to call house_robber on nums without first/last house and compare them
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
        
    def helper(self, nums): # house_robber I
        dp = [0]*len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[0]
            elif i == 1:
                dp[1] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
