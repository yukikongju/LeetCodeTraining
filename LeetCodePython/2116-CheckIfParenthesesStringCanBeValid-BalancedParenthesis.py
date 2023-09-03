#  https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/

class Solution:
    def canBeValid(self, string: str, locked: str) -> bool:
        # solution: balanced parenthesis

        # --- base case: length is odd
        if len(string) % 2 == 1:
            return False

        # --- Forward pass: check if too many ) => tot + op - cl < 0 return False
        tot, op, cl = 0, 0, 0
        for s, l in zip(string, locked):
            if l == '0': tot += 1
            elif s == '(': op += 1
            elif s == ')': cl += 1

            if tot + op - cl < 0: return False

        # --- Backward pass: check if too many ( => tot + cl - op < 0 return False
        tot, op, cl = 0, 0, 0
        for s, l in zip(reversed(string), reversed(locked)):
            if l == '0': tot += 1
            elif s == '(': op += 1
            elif s == ')': cl += 1

            if tot + cl - op < 0: return False
        
        return True

