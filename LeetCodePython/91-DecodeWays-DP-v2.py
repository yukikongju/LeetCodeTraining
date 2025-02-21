#  https://leetcode.com/problems/decode-ways/submissions/1550190712/
class Solution:
    def numDecodings(self, s: str) -> int:
        # solution: 1D DP - consider if we take last digit is valid and if last two digits are valid
        # last digit is valid ie not 0 => dp[i] += dp[i-1]
        # last 2 digits valid ie between 1 and 26 => dp[i] += dp[i-2]
        # edge case: i == 1: dp[1] = dp[0] + 1 if valid

        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 0 if s[0] == '0' else 1

        for i in range(1, n):
            # check if current digit is valid 
            if s[i] != '0':
                dp[i] += dp[i-1]
            
            # check if last 2 digits is valid
            if 1 <= int(s[i-1:i+1]) <= 26 and s[i-1] != '0':
                if i == 1:
                    dp[i] += 1
                else: 
                    dp[i] += dp[i-2]
        
        return dp[n-1]
        
