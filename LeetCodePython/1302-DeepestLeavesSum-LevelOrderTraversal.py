#  https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # solution: Level Order Traversal

        if not root:
            return 0

        # --- get level sum of each level
        res = []
        queue = [root]
        while queue:
            next_level, total = [], 0
            
            for node in queue:
                total += node.val
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            
            res.append(total)
            queue = next_level

        # --- return last level sum
        return res[-1]
