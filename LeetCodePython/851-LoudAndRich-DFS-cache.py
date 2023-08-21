#  https://leetcode.com/problems/loud-and-rich/

class Solution:
    def loudAndRich(self, richers: List[List[int]], quiet: List[int]) -> List[int]:
        # solution: DFS
        # To cut down the number of dfs we do, we have to start iterating from the least quiet first and only 
        # run dfs if the value hasn't been updated

        # --- Build Graph 
        n = len(quiet)
        precedances = {i: [] for i in range(n)}
        updated = [False for _ in range(n)]

        # --- order 
        order = sorted(list(range(n)), key=lambda i: quiet[i])

        for richer, poorer in richers:
            precedances[richer].append(poorer)
        
        def dfs(i, prec, val):
            if (val < quiet[i]) and (quieter[i] > val):
                solutions[i] = prec
                quieter[i] = val
                updated[i] = True

            for idx_next in precedances[i]:
                if not updated[idx_next]:
                    dfs(idx_next, prec, val)


        # --- 
        solutions = [i for i in range(n)]
        quieter = [q for q in quiet]

        for o in order:
            dfs(o, o, quiet[o])
        
        return solutions

