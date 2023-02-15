#  https://leetcode.com/problems/min-stack/
# NeetCode

#  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Sol: we keep two stack: one normal stack and one for the minimum element at 
# a given position

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

