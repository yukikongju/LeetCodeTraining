#  https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # solution: Inorder traversal + check if incrementing

        # --- inorder traversal
        traversal = [] 
        def inorder(node):
            if node.left: inorder(node.left)
            traversal.append(node.val)
            if node.right: inorder(node.right)

        inorder(root)
        
        # --- check if element are in increasing order
        for i in range(1, len(traversal)):
            if traversal[i] <= traversal[i-1]: return False
        return True
                
