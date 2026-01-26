class Trie:
    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        cur = self.d

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur['"'] = '' # end

    def search(self, word: str) -> bool:
        cur = self.d
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        return '"' in cur.keys()

    def startsWith(self, prefix: str) -> bool:
        cur = self.d
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True
# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))