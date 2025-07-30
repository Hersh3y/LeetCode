def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    table = []
    for i in range(len(text1) + 1):
        table.append([0] * (len(text2) + 1))
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i-1] == text2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[len(text1)][len(text2)]


print(longestCommonSubsequence("abcde", "ace")) # Output: 3
print(longestCommonSubsequence("abcde", "ace")) # Output: 3
print(longestCommonSubsequence("abc", "def")) # Output: 0
print(longestCommonSubsequence("cat", "crabt")) # Output: 3