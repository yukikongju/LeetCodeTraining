#  https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # solution: Tree to Graph + BFS

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

        # --- BFS
        levels = []
        visited = set()
        queue = [target.val]
        while queue:
            level, next_level = [], []
            for node in queue:
                level.append(node)
                visited.add(node)
                for neighbor in neighbors[node]:
                    if neighbor not in visited:
                        next_level.append(neighbor)
            
            queue = next_level
            levels.append(level)

        return levels[k] if len(levels) > k else [] 
        


