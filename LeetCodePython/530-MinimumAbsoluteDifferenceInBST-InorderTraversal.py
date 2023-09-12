#  https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # solution: In-order Traversal
        # inorder traversal: left child -> node -> right node
        
        def inorder_traversal(node):
            nonlocal prev_val, min_diff

            if node is None:
                return

            inorder_traversal(node.left)
            if prev_val is not None:
                min_diff = min(min_diff, abs(node.val - prev_val))
            prev_val = node.val
            inorder_traversal(node.right)
        
        prev_val = None
        min_diff = float('inf')
        inorder_traversal(root)
        return min_diff
