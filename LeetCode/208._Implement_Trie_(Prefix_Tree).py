class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)] # considering all is in lowercase & 
                                                    # indices: [0-25]
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        r = self.root
        for each_char in word:
            idx = ord(each_char) - ord('a')
            if not r.children[idx]: # is None
                r.children[idx] = TrieNode()
            r = r.children[idx]

        r.isEndOfWord = True

    def search(self, word: str) -> bool: ## TC: O(m), m = word length
        r = self.root
        for each_char in word:
            idx = ord(each_char) - ord('a')
            if not r.children[idx]: # is None
                return False
            r = r.children[idx]
        return True if r.isEndOfWord else False

    def startsWith(self, prefix: str) -> bool: ## TC: O(m), m = prefix length
        r = self.root
        for each_char in prefix:
            idx = ord(each_char) - ord('a')
            if not r.children[idx]: # is None
                return False
            r = r.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)