#  https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # solution: traversal

        if not root:
            return 0

        stack = [root]
        num_nodes = 0
        while stack:
            node = stack.pop(0)
            num_nodes += 1
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return num_nodes

        
