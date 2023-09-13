#  https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # solution: Graph BFS

        # --- build graph from tree
        neighbors = defaultdict(list)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                neighbors[node.val].append(node.left.val)
                neighbors[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                neighbors[node.val].append(node.right.val)
                neighbors[node.right.val].append(node.val)
                queue.append(node.right)
        
        # --- run BFS on graph
        minutes = 0
        visited = set()
        queue = [start]
        while queue:
            minutes += 1
            next_level = []
            for node in queue:
                visited.add(node)
                for neighbor in neighbors[node]:
                    if neighbor not in visited:
                        next_level.append(neighbor)
            queue = next_level
        
        return minutes-1
