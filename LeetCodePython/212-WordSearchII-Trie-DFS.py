#  https://leetcode.com/problems/word-search-ii/

class TrieNode: 
    def __init__(self):
        self.children = {}
        self.is_terminal = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_terminal = True
        node.word = word # store full word at terminal node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # solution: trie + dfs
        res = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])

        def dfs(node, i, j):
            char = board[i][j]
            if char not in node.children:
                return 
            
            next_node = node.children[char]
            if next_node.is_terminal:
                res.add(next_node.word)
                # next_node.is_terminal = False # avoid duplicates
            
            # mark cell as visited
            board[i][j] = '#'
            
            # visit neighbor if not visited and if in the trie
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if (0 <= x < m) and (0 <= y < n) and (board[x][y] in next_node.children):
                    dfs(next_node, x, y)

            # unmark cell as visited
            board[i][j] = char

            # if the current node has no children, remove it from trie
            if not node.children:
                node.remove(char)

        # --- add all words to Trie
        trie = Trie()
        for word in words:
            trie.add(word)

        # --- perform dfs on all cells
        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j)

        return list(res)
        
