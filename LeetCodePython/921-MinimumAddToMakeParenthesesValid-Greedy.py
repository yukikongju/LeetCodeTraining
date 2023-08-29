#  https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        # solution: Greedy

        # ---
        stack = []
        for s in string:
            if stack == [] or s == '(':
                stack.append(s)
            elif stack and stack[-1] == '(' and s == ')':
                stack.pop()
            else:
                stack.append(s)


        # ---
        return len(stack)
