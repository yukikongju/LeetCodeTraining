#  https://leetcode.com/problems/palindrome-pairs/description/?envType=problem-list-v2&envId=trie

# Solution: Trie
# Strategy:
# - Add every word to Trie
# - two words are palindrome if
#   (1) exact reverse => "abcd" and "dcba"
#   (2) word prefix is reverse and suffix is palindrome => "lls" ; "ll" is palindrome + "s" is in trie

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.pal_prefix = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def is_pal(self, s):
        return s == s[::-1]

    def add(self, word, index):
        node = self.root
        for i, c in enumerate(word):
            # If the remaining suffix of *original* word is palindrome
            # (because we're inserting reversed)
            if self.is_pal(word[i:]):
                node.pal_prefix.append(index)

            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]

        node.idx = index
        node.pal_prefix.append(index)

    def search(self, word, index):
        node = self.root
        res = []

        for i, c in enumerate(word):
            # Case 1: found a word end in Trie, and your suffix is palindrome
            if node.idx >= 0 and node.idx != index and self.is_pal(word[i:]):
                res.append([index, node.idx])

            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return res
            node = node.children[idx]

        # Case 2: words that ended *below* this node with palindrome prefix
        for j in node.pal_prefix:
            if j != index:
                res.append([index, j])

        return res


class Solution:
    def palindromePairs(self, words):
        trie = Trie()

        # Insert reversed words
        for i, word in enumerate(words):
            trie.add(word[::-1], i)

        res = []
        for i, word in enumerate(words):
            pairs = trie.search(word, i)
            res.extend(pairs)

        return res

