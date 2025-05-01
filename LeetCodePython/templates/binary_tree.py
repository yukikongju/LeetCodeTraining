# Types of traversal (TODO)
# - Inorder
# - preorder
# - postorder
# - level order

from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """ BFS """
    if not root:
        return
    result = []
    queue = deque([root])
    while queue:
        level = []
        next_queue = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        result.append(level)
        queue = next_queue
    return result

