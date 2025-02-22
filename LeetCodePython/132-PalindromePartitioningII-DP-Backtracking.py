#  https://leetcode.com/problems/palindrome-partitioning-ii/description/

class Solution:
    def minCut(self, s: str) -> int:
        # solution: DP + backtracking - Space Limit exceeded
        # intuition: use DP to compute all palindrome and backtracking to compute valid partition and return length of shortest result - 1

        # --- find all palindrome using DP - expand from the middle
        res = []
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for j in range(n):
            for i in range(j):
                if (s[i] == s[j]) and (dp[i+1][j-1] or i+1 == j):
                    dp[i][j] = True
        
        # --- generate all partitions using backtracking
        def backtrack(index, current):
            if index >= n:
                res.append(list(current))
            for k in range(index, n):
                if dp[index][k]:
                    current.append(s[index:k+1])
                    backtrack(k+1, current)
                    current.pop()
        
        backtrack(0, [])
        print(res)
        
        # --- finding the minimum cut
        smallest = min([len(partition) for partition in res])
        return 0 if smallest == 0 else smallest - 1
