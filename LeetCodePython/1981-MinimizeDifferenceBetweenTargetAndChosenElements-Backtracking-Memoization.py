#  https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # solution: Backtracking + memoization

        # ---
        m, n = len(mat), len(mat[0])
        dp = defaultdict(defaultdict)

        # --- sorting
        for i in range(m):
            mat[i] = sorted(mat[i])

        # ---
        global_min = float('inf')
        def backtrack(k, partial_sum):
            nonlocal global_min
            if k == m:
                global_min = min(global_min, abs(target - partial_sum))
                return abs(target - partial_sum)
            if partial_sum - target > global_min: 
                return float('inf')
            if (k in dp) and (partial_sum in dp[k]):
                return dp[k][partial_sum]
            
            min_diff = float('inf')
            for j in range(n):
                diff = min(min_diff, backtrack(k+1, partial_sum + mat[k][j]))
                if diff == 0:
                    min_diff = 0
                    break
                min_diff = min(min_diff, diff)

            dp[k][partial_sum] = min_diff
            return min_diff
        
        return backtrack(0, 0)

