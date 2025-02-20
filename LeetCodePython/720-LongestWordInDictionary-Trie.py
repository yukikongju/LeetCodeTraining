#  https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_terminal = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # solution: trie
        # we build the trie and for each word, we check if each letter is terminal

        # --- building the trie
        trie = Trie()
        for word in words:
            trie.add(word)
        
        # --- 
        longest = ''
        for word in words:
            can_be_built = True

            node = trie.root
            for char in word: 
                if char not in node.children or not node.children[char].is_terminal:
                    can_be_built = False
                    break
                node = node.children[char]
            
            if can_be_built and (len(word) > len(longest) or (len(word) == len(longest) and word < longest)):
                longest = word
        
        return longest


        
