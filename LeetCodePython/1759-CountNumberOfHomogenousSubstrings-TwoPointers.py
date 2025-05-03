#  https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        # solution: two pointers
        n = len(s) 
        left, right = 0, 0
        ans = 0
        current = 0 # current length
        MOD = 10**9 + 7

        while right < n:
            if s[right] == s[left]:
                current += 1
                right += 1
            else:
                current = 0
                left = right
            ans += current % MOD

        return ans % MOD
