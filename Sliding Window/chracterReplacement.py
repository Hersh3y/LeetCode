def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    longest = 0
    most_freq = 0
    hashmap = {}
    l = 0
    for r in range(len(s)):
        if s[r] not in hashmap:
            hashmap[s[r]] = 0
        hashmap[s[r]] += 1
        most_freq = max(hashmap.values())
        if (r - l + 1 - most_freq) > k:
            hashmap[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest


print(characterReplacement("ABAB", 2)) # Outputs 4
print(characterReplacement("AABABBA", 1)) # Outputs 4
print(characterReplacement("XYYX", 2)) # Outputs 4
print(characterReplacement("AAABABB", 1)) # Outputs 5