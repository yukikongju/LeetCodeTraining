#  https://leetcode.com/problems/remove-k-digits/description/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # solution: Greedy + Stack

        # ---
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        
        # ---
        stack = stack[:len(stack)-k]
        
        # --- remove leading zeroes
        while stack and stack[0] == "0":
            stack.pop(0)

        # ---         
        return "0" if stack == [] else "".join(stack)

