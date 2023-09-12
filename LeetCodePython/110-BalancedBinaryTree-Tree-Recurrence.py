#  https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # solution: 
        # check if height root.left and root.right differ by at most 1

        def max_height_difference(root):
            if root is None: return 0
            left_height, right_height = max_height_difference(root.left), max_height_difference(root.right)
            if (left_height < 0) or (right_height < 0) or abs(left_height - right_height) > 1: return -1
            return max(left_height, right_height) + 1
        
        return max_height_difference(root) >= 0
