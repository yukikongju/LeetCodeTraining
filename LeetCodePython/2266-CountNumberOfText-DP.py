#  https://leetcode.com/problems/count-number-of-texts/

class Solution:
    def countTexts(self, keys: str) -> int:
        # solution: 1D DP
        # intuition: checked pressed keys

        MOD = 10**9+7
        n = len(keys)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1 # one way to decode empty string

        for i in range(n):
            dp[i+1] += dp[i]
            if i >= 1 and keys[i] == keys[i-1]:
                dp[i+1] += dp[i-1]
            if i >= 2 and keys[i] == keys[i-1] == keys[i-2]:
                dp[i+1] += dp[i-2]
            if i >= 3 and keys[i] == keys[i-1] == keys[i-2] == keys[i-3] and keys[i] in '79':
                dp[i+1] += dp[i-3]
            
            dp[i+1] %= MOD
        
        return dp[-1]


