#  https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # solution: stack
        # (1) same direction -> append ; nothing in stack -> append
        # (2) opposite direction:
        #       - last == next => pop last
        #       - last < next => pop last
        #       - last > next => do nothing
        # if last <0 and next >0 => they go in opposite direction

        # ---
        stack = []
        for asteroid in asteroids:
            while stack and (stack[-1] > 0 and asteroid < 0) and (abs(stack[-1]) < abs(asteroid)):
                stack.pop()
            if (not stack) or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid <0) or (stack[-1] <0 and asteroid > 0):
                stack.append(asteroid)
            elif stack and (abs(stack[-1]) == abs(asteroid)):
                stack.pop()

        return stack

