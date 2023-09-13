#  https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # solution: postorder => left child ; right child ; parent

        res = []
        def postorder(node):
            for child in node.children:
                postorder(child)
            res.append(node.val)

        if root: postorder(root)
        return res
        
