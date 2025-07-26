def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    words = set(wordDict)
    table = [False] * (len(s) + 1)
    table[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if table[j] and s[j:i] in words:
                table[i] = True
    return table[len(s)]


print(wordBreak("leetcode", ["leet","code"])) # Output: True
print(wordBreak("applepenapple", ["apple","pen"])) # Output: True
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # Output: False
print(wordBreak("catsincars", ["cats","cat","sin","in","car"])) # Output: False