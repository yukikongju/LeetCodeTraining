#  https://leetcode.com/problems/remove-duplicate-letters/description/

class Solution:
    def removeDuplicateLetters(self, string: str) -> str:
        # solution: Monotonic Stack + HashMap

        # --- init: dict with biggest index of each letter
        idx_dict = defaultdict(int)
        for i, s in enumerate(string):
            idx_dict[s] = i

        # --- forward pass: get result
        seen, stack = set(), []
        for i, s in enumerate(string):
            if s not in seen:
                while stack and stack[-1] > s and i < idx_dict[stack[-1]]:
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(s)
                seen.add(s)
        
        return ''.join(stack)

