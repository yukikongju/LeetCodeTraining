class Solution:
    def jump(self, nums: List[int]) -> int:
        # sol: greedy => we calculate how many jumps if required to reach ith position
        # at each position, what's the furthest we can reach 

        n = len(nums)
        dp = [float('inf') for _ in nums]
        dp[-1] = 0 
        for i in range(len(nums) -2, -1, -1):
            # can we jump directly to the end
            if i + nums[i] >= n - 1:
                dp[i] = 1
            else: # where to jump at
                min_jumps = float('inf')
                for jump in range(1, nums[i]+1):
                    min_jumps = min(min_jumps, 1 + dp[i + jump])
                dp[i] = min_jumps
        return dp[0]


