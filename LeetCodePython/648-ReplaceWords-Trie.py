#  https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        node = self.root
        for char in word: 
            if char not in node.children: 
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # solution: Trie
        # build a Trie with dictionary. For each word in the sentence, replace with substring if found in Trie

        # --- build trie 
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        

        # --- replace in sentence
        res = []
        for word in sentence.split():
            # check if substring is found 
            node = trie.root
            for i, char in enumerate(word):
                if char not in node.children or node.is_word:
                    break
                node = node.children[char]
                
            if node.is_word:
                if i == 0: i = 1 # edge case: 
                res.append(word[:i])
            else:
                res.append(word)
        
        return ' '.join(res)
        
