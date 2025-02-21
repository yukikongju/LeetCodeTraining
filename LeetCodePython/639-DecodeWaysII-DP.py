#  https://leetcode.com/problems/decode-ways-ii/

class Solution:
    def numDecodings(self, s: str) -> int:
        # solution: 1D DP

        if s[0] == '0': 
            return 0
        
        MOD = 10**9 + 7
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1 # one way to decode empty string
        dp[1] = 9 if s[0] == '*' else 1

        for i in range(1, n):
            if s[i] == '*':
                # last digit
                dp[i+1] += 9 * dp[i]
                # two last digits
                if s[i-1] == '1':
                    dp[i+1] += 9 * dp[i-1]
                elif s[i-1] == '2':
                    dp[i+1] += 6 * dp[i-1]
                elif s[i-1] == '*':
                    dp[i+1] += 15 * dp[i-1]
            else:
                if s[i] != '0':
                    dp[i+1] += dp[i]
                if s[i-1] == '*' and 0 <= int(s[i]) <= 6:
                    dp[i+1] += 2 * dp[i-1]
                elif s[i-1] == '*' and 7 <= int(s[i]) <= 9:
                    dp[i+1] += dp[i-1]
                elif s[i-1] == '1' or (s[i-1] == '2' and 0 <= int(s[i]) <= 6):
                    dp[i+1] += dp[i-1]

            dp[i+1] %= MOD
            if not dp[i+1]:
                return 0

        return dp[n]


        
