def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longest = ""
    longest_length = 0
    for i in range(len(s)):
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > longest_length:
                longest = s[l:r+1]
                longest_length = r - l + 1
            l -= 1
            r += 1
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > longest_length:
                longest = s[l:r+1]
                longest_length = r - l + 1
            l -= 1
            r += 1
    return longest


print(longestPalindrome("babad")) # Output: bab
print(longestPalindrome("cbbd")) # Output: bb
print(longestPalindrome("abcdedcba")) # Output: abcdedcba