#  https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/description/

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # DP + Memoization
        MOD = 10**9 + 7

        # z: num_zeros remaining; o: num_ones remaining; p: previous choice (0 or 1)
        @cache
        def dp(z: int, o: int, p: int):
            if z == 0 and o == 0:
                return 1
            else: 
                answer = 0 
                for i in range(1, limit+1):
                    if (p == 0 or p == -1) and (o-i >= 0):
                        answer += dp(z, o-i, 1)
                    if (p == 1 or p == -1) and (z-i >= 0):
                        answer += dp(z-i, o, 0)
                return answer % MOD
        
        return dp(zero, one, -1) % MOD

