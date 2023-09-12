#  https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # solution: Tree DFS
        # diameter = longest path root.left + longest path root.right
        diameter = 0

        def depth(node):
            nonlocal diameter
            left = depth(node.left) if node.left else 0
            right = depth(node.right) if node.right else 0
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return diameter

