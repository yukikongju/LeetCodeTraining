#  https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/submissions/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # solution: Monotonic Stack
        # we add to stack and pop if the element we iterate at is smaller than last element in the stack

        # --- build dictionary of letter's last index 
        idx_dict = {}
        for i, letter in enumerate(s):
            idx_dict[letter] = i
        

        # --- monotonic stack
        stack, seen = [], set()
        for i, letter in enumerate(s):
            if letter not in seen:
                while stack and stack[-1] > letter and idx_dict[stack[-1]] > i:
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(letter)
                seen.add(letter)
        

        return ''.join(stack)



