#  https://www.geeksforgeeks.org/trie-insert-and-search/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True


if __name__ == "__main__":
    trie = Trie()
    words = ["and", "ant", "do", "dad"]
    for w in words:
        trie.insert(w)

    searches = ["an", "and", "d", "daddy"]
    for w in searches:
        print(trie.search(w), end=" ")

    print()
    prefixes = ["an", "and", "d", "daddy"]
    for w in prefixes:
        print(trie.startsWith(w), end=" ")
