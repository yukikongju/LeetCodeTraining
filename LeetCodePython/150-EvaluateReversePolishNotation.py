#  https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#  NeetCode:

# Solution: iterate from left to right. If we see a number, add it to stack; 
# if it is an operator, pop the last two elements and append the result to 
# the stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else: 
                stack.append(int(token))
        return stack[0]
