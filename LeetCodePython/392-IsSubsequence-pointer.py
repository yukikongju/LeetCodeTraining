#  https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # solution: pointer
        ps, pt = 0, 0 
        m, n = len(s), len(t)

        while ps < m and pt < n:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        
        return True if ps == m else False
        
