#  https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # solution: two pointers

        # --- best sol changing pointers end
        n = len(colors)
        start, end = 0, n-1
        while start <= end and (colors[start] == colors[end]):
            end -= 1
        
        sol_left = end - start

        # --- best sol changing pointers start
        start, end = 0, n-1
        while start <= end and (colors[start] == colors[end]):
            start += 1
        
        sol_right = end-start

        return max(sol_left, sol_right)
        
