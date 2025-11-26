#  https://leetcode.com/problems/map-sum-pairs/?envType=problem-list-v2&envId=trie

# Solution: Trie
# Strategy:
# - when inserting new key, traverse the whole word in trie and increment each node
# - If the key already exist we need to override

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        # self.end = False
        self.val = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        node = self.root
        diff = val - self.map[key]
        for c in key:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node.children[idx].val += diff
            node = node.children[idx]
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return 0
            node = node.children[idx]
        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
