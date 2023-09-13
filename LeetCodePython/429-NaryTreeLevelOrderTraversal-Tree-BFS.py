#  https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # solution: BFS level order traversal

        # --- base case
        if not root: return []
        if root and not root.children:
            return [[root.val]]

        # --- level order traversal
        res = []
        queue = [root]
        while queue: 
            level, next_level = [], []
            for node in queue:
                level.append(node.val)
                for child in node.children:
                    next_level.append(child)
            
            res.append(level)
            queue = next_level

        # ---
        return res


        
