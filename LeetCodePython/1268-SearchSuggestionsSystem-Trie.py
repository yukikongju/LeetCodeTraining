#  https://leetcode.com/problems/search-suggestions-system/description/?envType=problem-list-v2&envId=trie

# Solution: Trie
# Strategy:
# 1. Add product to Trie
# 2. Get K Suggestions
# Notes:
# - we don't want to traverse the whole word every time, so we need to remember previous node

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.end = True
        node.word = word
    
    def dfs(self, node: TrieNode, suggestions: List[int], K: int = 3): # DFS
        if not node or len(suggestions) == K:
            return 
        
        if node.end:
            suggestions.append(node.word)
        
        for i in range(26):
            if node.children[i]:
                self.dfs(node.children[i], suggestions, K)
    
    def get_suggestions(self, node: TrieNode):
        if not node:
            return []
        suggestions = []
        self.dfs(node, suggestions)
        return suggestions

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        trie = Trie()
        for product in products:
            trie.add(product)
        
        res = []
        node = trie.root
        fails = False
        for c in searchWord:
            # if fails:
            #     res.append([])
            #     continue

            idx = ord(c) - ord('a')
            if not node.children[idx]:
                # fails = True
                # res.append([])
                # continue
                break

            node = node.children[idx]
            suggestions = trie.get_suggestions(node)
            res.append(suggestions)
        
        # if searchWord not in trie, then pad with empty suggestions
        missing = len(searchWord) - len(res)
        for _ in range(missing):
            res.append([])
        
        return res
