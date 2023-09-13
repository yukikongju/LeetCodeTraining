#  https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # solution: traversal: parent -> left child -> right child

        num_good_nodes = 0

        def traversal(node, max_val):
            nonlocal num_good_nodes

            if node.val >= max_val:
                num_good_nodes += 1
            max_val = max(max_val, node.val)
            if node.left: traversal(node.left, max_val)
            if node.right: traversal(node.right, max_val)
        
        if root:
            traversal(root, float('-inf'))
        
        return num_good_nodes
            

