#  https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # solution: postorder traversal => left child ; right child ; parent

        res = []

        def postorder(node):
            if node.left: postorder(node.left)
            if node.right: postorder(node.right)
            res.append(node.val)
        
        if root:
            postorder(root)
        
        return res
        
