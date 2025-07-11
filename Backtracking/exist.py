def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    row_length = len(board)
    col_length = len(board[0])
    visited = set()

    def backtrack(r, c, size):
        if size == len(word):
            return True
        if r < 0 or c < 0 or r >= row_length or c >= col_length or board[r][c] != word[size] or (r, c) in visited:
            return False
        visited.add((r, c))
        if backtrack(r+1, c, size+1) or backtrack(r-1, c, size+1) or backtrack(r, c+1, size+1) or backtrack(r, c-1, size+1):
            return True
        else:
            visited.remove((r, c))
            return False
    
    for i in range(row_length):
        for j in range(col_length):
            if backtrack(i, j, 0):
                return True
    return False


print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # Output: True
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # Output: True
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # Output: False
print(exist([
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
], "CAT")) # Output: True
print(exist([
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
], "BAT")) # Output: False