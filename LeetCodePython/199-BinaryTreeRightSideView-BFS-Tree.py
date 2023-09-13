#  https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # solution: BFS Tree

        res = []
        queue = [root]
        while queue:
            level, next_level = [], []
            
            for node in queue:
                if node:
                    level.append(node.val)
                    if node.left: next_level.append(node.left)
                    if node.right: next_level.append(node.right)
            
            if level: 
                res.append(level[-1]) 
            queue = next_level
            
        return res
