#  https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # solution: DFS

        if not root:
            return []

        res = []
        def dfs(node, path, current_sum):
            if node and (not node.left) and (not node.right) and (node.val + current_sum == targetSum):
                res.append(path + [node.val])
            if node.left:
                dfs(node.left, path + [node.val], current_sum + node.val)
            if node.right:
                dfs(node.right, path + [node.val], current_sum + node.val)
        
        dfs(root, [], 0)

        return res
        
