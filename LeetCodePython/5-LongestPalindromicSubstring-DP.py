#  https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # solution: 2D-DP 
        # intuition: i and j will be the slicing index and we expand from the middle 
        # => if odd: s[i] == s[j] and dp[i+1][j-1]
        # => if even: s[i] == s[j] and i = j + 1

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        longest = s[0]
        for j in range(n):
            for i in range(j):
                if s[i] == s[j] and (dp[i+1][j-1] or i+1 == j):
                    dp[i][j] = True

                    if j - i + 1 > len(longest):
                        longest = s[i: j+1]

        return longest

        
