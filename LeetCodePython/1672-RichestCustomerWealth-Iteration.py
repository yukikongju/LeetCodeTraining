class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # solution: iteration
        max_wealth = 0 
        for account in accounts:
            wealth = 0
            for amount in account:
                wealth += amount
            max_wealth = max(wealth, max_wealth)
        return max_wealth
        
