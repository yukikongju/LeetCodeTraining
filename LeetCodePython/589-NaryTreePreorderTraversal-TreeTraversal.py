#  https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # solution: preorder => parent ; left child ; right child

        res = []
        
        def traversal(node):
            res.append(node.val)
            for child in node.children:
                traversal(child)
        
        if root:
            traversal(root)
        
        return res
        
