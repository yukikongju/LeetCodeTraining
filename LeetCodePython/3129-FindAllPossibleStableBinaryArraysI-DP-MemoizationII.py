#  https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
# Note: this implementation is a lot slower than using the @cache decorator

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        memo = {}
        MOD = 10**9 + 7

        def dp(z, o, p):
            if z == 0 and o == 0:
                return 1
            
            if (z, o, p) in memo:
                return memo[(z, o, p)]
            
            answer = 0
            for i in range(1, limit+1):
                if (p == 0 or p == -1) and (o-i>=0):
                    answer += dp(z, o-i, 1)
                if (p == 1 or p == -1) and (z-i>=0):
                    answer += dp(z-i, o, 0)
            
            memo[(z, o, p)] = answer % MOD
            return memo[(z, o, p)]
        
        return dp(zero, one, -1) % MOD
        
        
