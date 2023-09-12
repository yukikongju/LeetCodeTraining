#  https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # on demande à chaque noeud si subRoot et le sous-arbre à partir de ce noeud est le même
        
        # parcourir root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)
            
            # check if subtree
            if self.isSameTree(subRoot, node):
                return True
            
            
        return False
        
        
    
    def isSameTree(self, t1, t2):
        if (t1 and not t2) or (not t1 and t2):
            return False
        if not t1 and not t2:
            return True
        else: 
            return (t1.val == t2.val) and (self.isSameTree(t1.left, t2.left)) and (self.isSameTree(t1.right, t2.right))
        
