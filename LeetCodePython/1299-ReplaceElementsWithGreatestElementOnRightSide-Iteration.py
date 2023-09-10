#  https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # solution: Iteration

        # --- base case
        if len(arr) == 1:
            return [-1]

        n = len(arr)
        res = [-1 for _ in range(n)]
        current = arr[-1]
        for i in range(n-2, -1, -1):
            res[i] = current
            current = max(current, arr[i])
        
        return res

