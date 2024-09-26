#  https://leetcode.com/problems/sum-of-prefix-scores-of-strings/submissions/1402421020/

class TrieNode:
    def __init__(self):
        self.prefix_count = 0
        self.children = {}

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # solution: Trie
        
        # insert all word in the trie
        root = TrieNode()
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.prefix_count += 1

        # count number of prefix using the trie
        res = []
        for word in words:
            current = root  
            score = 0
            for char in word:
                current = current.children[char]
                score += current.prefix_count
            res.append(score)
        
        return res
