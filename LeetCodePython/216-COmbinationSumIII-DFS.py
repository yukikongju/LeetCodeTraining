#  https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # solution:

        # ---
        sols = []
        def dfs(v, current_sum):
            if (len(v) == k) and current_sum == n:
                sols.append(v)
            
            visited = set(v)
            start = v[-1] if v else 1
            for i in range(start, 10):
                if (i not in visited) and (current_sum + i <= n):
                    w = v + [i]
                    dfs(w, current_sum + i)
        
        dfs([], 0)
        return sols
