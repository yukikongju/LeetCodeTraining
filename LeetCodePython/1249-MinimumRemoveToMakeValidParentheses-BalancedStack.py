
#  https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

class Solution:
    def minRemoveToMakeValid(self, string: str) -> str:
        # solution: Balanced Stack
        
        stack = []
        balance = 0

        # --- only add ) if they have a matching (
        for i, s in enumerate(string):
            stack.append(s)
            if s == '(':
               balance += 1
            elif s == ')':
                if balance > 0: # more open than closed
                    balance -= 1
                else: # we don't add the closed parenthesis
                    stack.pop()


        # --- remove all additional open parentheses starting at the end
        last = len(stack) -1
        while (last>=0) and (balance>0):
            if stack[last] == '(':
                stack[last] = ''
                balance -= 1
            last -= 1
        
        # ---
        return ''.join(stack)

