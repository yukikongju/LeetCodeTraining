#  https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # solution: BFS-ish

        # --- 
        queue = [(root, None)] # (node, parent)
        while queue: 
            next_level = []

            x_parent, y_parent = None, None
            for node, parent in queue:
                if node.val == x: x_parent = parent
                elif node.val == y: y_parent = parent

                if x_parent and y_parent: 
                    return x_parent != y_parent
                
                if node.left: next_level.append((node.left, node))
                if node.right: next_level.append((node.right, node))
            
            queue = next_level

        return False

        
