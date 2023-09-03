#  https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution:
    def checkValidString(self, string: str) -> bool:
        # solution: Balanced Parenthesis - Forward-Backward pass
        # The string is invalid only if we have more open/close parenthesis

        # --- Forward Pass: check if we have too much )
        tot, op, cl = 0, 0, 0
        for s in string:
            if s == '*': tot += 1
            elif s == '(': op += 1
            elif s == ')': cl += 1

            if tot + op - cl < 0: return False

        # --- Backward Pass: check if we have too much (
        tot, op, cl = 0, 0, 0
        for s in reversed(string):
            if s == '*': tot += 1
            elif s == '(': op += 1
            elif s == ')': cl += 1

            if tot + cl - op < 0: return False

        
        return True
        

