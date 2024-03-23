class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # solution: greedy // monotonic array
        # do task with highest difference of energy first

        # --- sort
        sorted_tasks = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)

        # ---
        ans = diff = 0
        for cost, mmin in sorted_tasks:
            if mmin > diff:
                ans += (mmin - diff)
                diff = mmin
            diff -= cost

        return ans
