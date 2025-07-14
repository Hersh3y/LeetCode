class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
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
        def backtrack(node, index):
            if len(word) == index:
                return node.word_end
            if word[index] == '.':
                for i in node.children.values():
                    if backtrack(i, index+1):
                        return True
                return False
            else:
                if word[index] in node.children:
                    return backtrack(node.children[word[index]], index+1)
                else:
                    return False
                
        return backtrack(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # Output: False
print(wordDictionary.search("bad")) # Output: True
print(wordDictionary.search(".ad")) # Output: True
print(wordDictionary.search("b..")) # Output: True

wordDictionary2 = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
print(wordDictionary.search("say")) # Output: False
print(wordDictionary.search("day")) # Output: True
print(wordDictionary.search(".ay")) # Output: True
print(wordDictionary.search("b..")) # Output: True
