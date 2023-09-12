#  https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # idee: utiliser une file pour ajouter parent et enfant 
        output = []
        queue = [root]
        
        if root == None:
            return []
        
        while len(queue) != 0 :
            children = []
            level = []
            
            for node in queue:
                if node:
                    level.append(node.val)
                    if node.left: 
                        children.append(node.left)
                    if node.right: 
                        children.append(node.right)

            output.append(level)
            queue = children
        
        return output

