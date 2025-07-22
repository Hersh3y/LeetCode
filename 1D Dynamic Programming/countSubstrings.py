def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    for i in range(len(s)):
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
    return result


print(countSubstrings("abc")) # Output: 3
print(countSubstrings("aaa")) # Output: 6