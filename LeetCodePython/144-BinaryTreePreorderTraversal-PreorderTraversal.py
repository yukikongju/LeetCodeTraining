#  https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # solution: preorder traversal => parent ; left child ; right child

        res = []
        def preorder(node):
            res.append(node.val)
            if node.left: preorder(node.left)
            if node.right: preorder(node.right)
        
        if root:
            preorder(root)
        
        return res
        
