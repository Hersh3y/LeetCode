class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.word_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in word:
            if i not in current.children:
                return False
            current = current.children[i]
        return current.word_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for i in prefix:
            if i not in current.children:
                return False
            current = current.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


trie1 = Trie()
trie1.insert("apple")
print(trie1.search("apple")) # Output: True
print(trie1.search("app")) # Output: False
print(trie1.startsWith("app")) # Output: True
trie1.insert("app")
print(trie1.search("app")) # Output: True
