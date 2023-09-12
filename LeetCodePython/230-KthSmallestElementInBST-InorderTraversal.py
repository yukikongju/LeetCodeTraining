#  https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # solution: Tree in-order traversal

        # ---
        traversal = []
        def inorder(node):
            if node.left: inorder(node.left)
            traversal.append(node.val)
            if node.right: inorder(node.right)

        inorder(root)
        return traversal[k-1]

