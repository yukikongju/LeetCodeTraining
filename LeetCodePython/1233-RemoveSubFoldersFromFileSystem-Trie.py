#  https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/?envType=problem-list-v2&envId=trie
# Solution: Trie - O(n)
# 1. Add folders to trie => if we pass through and we see a terminal node, it's a subfolder and we don't add it
# 2. To find the root folders, traverse all child to find terminal node

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, subfolder: str) -> None:
        node = self.root
        is_subfolder = False
        for s in subfolder[1:].split('/'):
            if node.end:
                is_subfolder = True
                break
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]

        if not is_subfolder: # remove all subfolder
            node.end = True
            node.children = {}
    
    def search(self, subfolder: int) -> bool:
        node = self.root
        for s in subfolder[1:].split('/'):
            if s not in node.children:
                return False
            node = node.children[s]
        return node.end


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        trie = Trie()

        # 1. add folders in trie if not subfolder
        for folder in folders:
            trie.add(folder)
        
        # 2. get root folder by checking if folder is terminal
        res = []
        for folder in folders:
            if trie.search(folder):
                res.append(folder)
        
        return res

