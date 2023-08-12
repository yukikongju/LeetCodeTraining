#  https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # solution: backtrack
        stack = []
        solutions = []

        def backtrack(num_open, num_closed):
            if num_open == num_closed == n:
                solutions.append("".join(stack))
            if num_open < n:
                stack.append('(')
                backtrack(num_open + 1, num_closed)
                stack.pop()
            if num_closed < num_open: 
                stack.append(')')
                backtrack(num_open, num_closed + 1)
                stack.pop()
        

        backtrack(0, 0)

        return solutions


        
            
