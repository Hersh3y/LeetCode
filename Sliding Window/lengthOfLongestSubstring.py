def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest = 0
    hashmap = {}
    l = 0
    for r in range(len(s)):
        if s[r] in hashmap and hashmap[s[r]] >= l:
            l = hashmap[s[r]] + 1
        hashmap[s[r]] = r
        longest = max(longest, r - l + 1)
    return longest


print(lengthOfLongestSubstring("abcabcbb")) # Outputs 3
print(lengthOfLongestSubstring("bbbbb")) # Outputs 1
print(lengthOfLongestSubstring("pwwkew")) # Outputs 3
print(lengthOfLongestSubstring("zxyzxyz")) # Outputs 3
print(lengthOfLongestSubstring("xxxx")) # Outputs 1