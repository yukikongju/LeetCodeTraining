#  https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # solution: Level Order Traversal + MaxHeap

        # --- Level Order traversal to find level sum + insert in maxHeap
        maxHeap = []
        queue = [root]
        while queue: 
            level, next_level = [], []
            total = 0
            for node in queue:
                # level.append(node)
                total += node.val
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            
            heapq.heappush(maxHeap, -total)
            queue = next_level


        # --- find kth largest sum
        if k > len(maxHeap): return -1
        for _ in range(k):
            kth_sum = heapq.heappop(maxHeap) * -1
        
        return kth_sum
