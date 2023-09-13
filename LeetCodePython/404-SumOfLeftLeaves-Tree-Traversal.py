#  https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # solution: inorder traversal
        # add value to total if node is leaf

        if root and not root.left and not root.right:
            return 0

        total = 0
        stack = [(root, False)] # (node, isLeft)
        while stack:
            node, is_left = stack.pop(0)
            if node and not node.left and not node.right:
                if is_left:
                    total += node.val
            if node.left: stack.append((node.left, True))
            if node.right: stack.append((node.right, False))
        
        return total


