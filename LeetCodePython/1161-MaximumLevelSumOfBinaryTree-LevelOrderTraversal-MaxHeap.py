#  https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # solution: Level Order Traversal + MaxHeap

        # --- level order traversal 
        maxHeap = [] # (level_sum, level)
        queue = [root]
        idx_level = 1
        while queue: 
            next_level = []
            total = 0
            for node in queue:
                total += node.val
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            heapq.heappush(maxHeap, (-total, idx_level))
            queue = next_level
            idx_level += 1

        # --- get level of maximum sum
        _, level = maxHeap[0]

        # ---
        return level

        
