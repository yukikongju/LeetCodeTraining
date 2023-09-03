#  https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/

class Solution:
    def minInsertions(self, string: str) -> int:
        # solution: String Replace
        # (1) for each '(', we need two '))' -> '}' => required_brackets
        # (2) for each ')' => missing_brackets

        # --- replace )) by }
        string = string.replace('))', '}')
        
        # ---
        required_brackets, missing_brackets = 0, 0
        for s in string:
            if s == '(':
                required_brackets += 2
            elif s == ')': 
                if required_brackets > 0: # we have ( and ), so we need to add 1
                    required_brackets -= 2
                    missing_brackets += 1
                else: # we only have ), so we need to add 2 -> add '(' and ')'
                    missing_brackets += 2
            elif s == '}':
                if required_brackets > 0:
                    required_brackets -= 2
                else: # need to add ( to match }
                    missing_brackets += 1

        # ---
        return required_brackets + missing_brackets

