#  https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, string: str) -> str:
        # solution: Stack
        # edge case: star, but no letter prior

        # --- 
        stack = []
        for s in string:
            if s != '*':
                stack.append(s)
            else:
                if stack: stack.pop()

        return ''.join(stack) 
