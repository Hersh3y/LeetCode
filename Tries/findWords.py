class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, word):
        current = self
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.word_end = True

def findWords(board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    root = TrieNode()
    for i in words:
        root.insert(i)
    row_length = len(board)
    col_length = len(board[0])
    result = set()
    visited = set()

    def backtrack(r, c, node, word):
        if r < 0 or c < 0 or r >= row_length or c >= col_length or board[r][c] not in node.children or (r, c) in visited:
            return
        node = node.children[board[r][c]]
        visited.add((r, c))
        word += board[r][c]
        if node.word_end:
            result.add(word)
        backtrack(r+1, c, node, word)
        backtrack(r-1, c, node, word)
        backtrack(r, c+1, node, word)
        backtrack(r, c-1, node, word)
        visited.remove((r, c))

    for i in range(row_length):
        for j in range(col_length):
            backtrack(i, j, root, "")
    return list(result)

# Output: ["eat","oath"]
print(findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(findWords([["a","b"],["c","d"]], ["abcb"])) # Output: []
print(findWords([
    ["a","b","c","d"],
    ["s","a","a","t"],
    ["a","c","k","e"],
    ["a","c","d","n"]
    ], ["bat","cat","back","backend","stack"]))  # Output: ['backend', 'cat', 'back']
print(findWords([
    ["x","o"],
    ["x","o"]
    ], ["xoxo"]))  # Output: []
