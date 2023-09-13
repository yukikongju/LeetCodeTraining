#  https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # solution: preorder traversal

        # --- traverse preorder to find all paths
        paths = []
        def preorder(node, path):
            if node and not node.left and not node.right:
                paths.append(path + [node.val])
            if node.left: preorder(node.left, path + [node.val])
            if node.right: preorder(node.right, path + [node.val])

        if root: preorder(root, [])

        # --- put paths in correct output form
        res = []
        for path in paths:
            res.append("->".join(map(str, path)))

        return res

