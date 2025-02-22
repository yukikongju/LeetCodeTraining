#  https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # solution: DP + Backtracking
        # intuition: \
        # (1) use dp to compute all palindrome - i, j will be slicing index and we expand from middle
        # (2) use backtracking to generate partitions - for each index, iterate through 
        # brute-force: partition all and test if its a palindrome => n!

        # --- find palindromes using DP
        # case 1: length >= 3 => expand from middle
        # case 2: len == 2 => check prev
        res = []
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for j in range(n):
            for i in range(j):
                if (s[i] == s[j]) and (dp[i+1][j-1] or i+1 == j):
                    dp[i][j] = True

        # --- generate partitions with backtracking
        def backtracking(index, current):
            if index >= n:
                res.append(list(current))
            for k in range(index, n):
                if dp[index][k]:
                    current.append(s[index:k+1])
                    backtracking(k + 1, current)
                    current.pop()

        backtracking(0, [])
        return res
        
