class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        cur = self.root

        for token in word:
            if token not in cur.children:
                cur.children[token] = TrieNode()
            cur = cur.children[token]

        cur.endOfWord = True

    def search(self, word: str) -> bool:

        cur = self.root

        for token in word:
            if token in cur.children:
                cur = cur.children[token]
            else: return False

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root

        for token in prefix:
            if token in cur.children:
                cur = cur.children[token]
            else: return False

        return True