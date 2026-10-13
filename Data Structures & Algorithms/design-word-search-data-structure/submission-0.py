class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        cur = self.root

        for token in word:
            if token not in cur.children:
                cur.children[token] = TrieNode()
            cur = cur.children[token]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                token = word[i]

                if "." == token:
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if token not in cur.children:
                        return False
                    cur = cur.children[token]

            return cur.endOfWord

        return dfs(0, self.root)