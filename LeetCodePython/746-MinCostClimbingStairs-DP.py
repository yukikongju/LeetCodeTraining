class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Sol: DP 1D
        dp = [0]*len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        
        return min(dp[-2:])
