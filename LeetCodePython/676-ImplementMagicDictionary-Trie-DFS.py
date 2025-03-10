#  https://leetcode.com/problems/implement-magic-dictionary/

class TrieNode: 
    def __init__(self):
        self.children = {}
        self.is_end = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            current = self.root
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = TrieNode()
                current = current.children[letter]
            current.is_end = True

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)

        def dfs(node: TrieNode, count: int, index: int) -> bool:
            if index == n: 
                return count == 1 and node.is_end
            return any([dfs(node.children[c], count + int(c != searchWord[index]), index + 1) for c in node.children])
        
        return dfs(self.root, 0, 0)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
