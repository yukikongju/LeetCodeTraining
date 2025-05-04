#  https://leetcode.com/problems/daily-temperatures/submissions/1625482835/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # solution: monotonic stack 
        n = len(temperatures)
        stack = []
        res = [0] * n 

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res
