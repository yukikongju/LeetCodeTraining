#  https://leetcode.com/problems/132-pattern/description/?envType=problem-list-v2&envId=monotonic-stack

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # solution: monotonic stack - strictly decreasing stack
        # intuitions: 
        # - prefixes: 
        # - stack: keep minimum

        stack = []
        current_min = nums[0]

        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            
            if stack and num > stack[-1][1]:
                return True
            
            stack.append([num, current_min])
            current_min = min(current_min, num)
        
        return False
