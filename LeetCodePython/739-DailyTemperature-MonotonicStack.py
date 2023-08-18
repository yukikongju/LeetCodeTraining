#  https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # sol: stack - monotonic decreasing sequence - O(n)

        # ---
        stack = [] # [temp, position]
        results = [0 for _ in range(len(temperatures))]

        # --- 
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                idx = stack.pop()[1]
                results[idx] = i - idx
            stack.append([temp, i])

        return results


