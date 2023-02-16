class Solution:
    def numDecodings(self, s: str) -> int:
        # DP: https://www.youtube.com/watch?v=W4rYz-kd-cY
        # (1) '12160': if s[i] == 0 and s[i-1] > 2: return 0 
        # (2) '12122': if s[i] != 0 and (s[]) : dp[i] = dp[i-1] + dp[i-2]
        # (3) '12129': if s[i-1:i+1] > 26: dp[i] = dp[i-1] (on concatene '9')
        # (4) '12120' or '12110': if s[i] == 0 and s[i-1] is 1 or 2: dp[i] = dp[i-2]
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        if s[0] == '0':
            return 0
        else:
            dp[1] = 1
        
        for i in range(2, len(s) + 1):
            if s[i-1] == '0':
                if s[i-2] == '1' or s[i-2] == '2': # 10, 20
                    dp[i] = dp[i-2]
                else: # 00, '30', '40', 
                    return 0 
            else:
                if (s[i-2] == '1') or (s[i-2] == '2' and int(s[i-1]) < 7): # 11-19, 21-26
                    dp[i] = dp[i-1] + dp[i-2]  
                else: # 01-09, x > 27
                    dp[i] = dp[i-1]

        return dp[len(s)]

