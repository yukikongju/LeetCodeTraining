#  https://leetcode.com/problems/short-encoding-of-words/?envType=problem-list-v2&envId=trie

# Solution: Trie
# Strategy:
# - Only keep words that are not suffixes of other words
# - Add each word in reverse. When adding new branch, check if existing node is terminal. If it is, remove terminal node
# - To find shortest reference string, go through list of words and only keep the one that are terminal

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')

            # node.end = False

            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.end
    
    def remove_terminal_prefix(self, word: int) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return
            node.end = False
            node = node.children[idx]


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()

        # 0. Remove duplicates and sort word by descending length
        words = list(set(words))
        words.sort(key=lambda x: len(x), reverse=True)
        
        # 1. add reversed word to trie
        for word in words:
            trie.add(word[::-1])
        
        # 2. remove words that are suffixes
        for word in words:
            trie.remove_terminal_prefix(word[::-1])

        # 3. Compute shortest reference string
        res = []
        for word in words:
            word = word[::-1]
            if trie.search(word):
                res.append(word)

        return sum([len(word) for word in res]) + len(res)
        

            

        
