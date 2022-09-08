#  Link: https://leetcode.com/problems/minimum-cost-for-tickets/

# Time Complexity: O(m*n)

# Follow-up: (1) What if there were more ticket ie bi-weekly, trimester, ...; 
# (2) What if rabais selon time of year or per ticket bought or money spent


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Solution: 1D DP => 
        
        num_days = days[-1]
        dp = [0 for _ in range(num_days+1)]
        
        for i in range(1, num_days +1):
            if i in days:
                dp[i] = min(dp[max(i-1, 0)] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
            else: 
                dp[i] = dp[i-1]
        
        return dp[-1]
        
