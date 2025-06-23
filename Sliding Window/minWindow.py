def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    need = {}
    for i in range(len(t)):
        if t[i] not in need:
            need[t[i]] = 0
        need[t[i]] += 1
    min_str = ""
    window = {}
    required = sum(need.values())
    valid = 0
    l = 0
    for r in range(len(s)):
        if s[r] not in window:
            window[s[r]] = 0
        window[s[r]] += 1
        if s[r] in need and window[s[r]] <= need[s[r]]:
            valid += 1
        if valid == required:
            if len(min_str) < valid:
                min_str = s[l:r+1]
            if r - l + 1 < len(min_str):
                min_str = s[l:r+1]
        while valid == required:
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                valid -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
            elif r - l < len(min_str):
                min_str = s[l+1:r+1]
            l += 1
    return min_str


print(minWindow("ADOBECODEBANC", "ABC")) # Output: BANC
print(minWindow("a", "a")) # Output: a
print(minWindow("a", "aa")) # Output: Empty String
print(minWindow("OUZODYXAZV", "XYZ")) # Output: YXAZ
print(minWindow("xyz", "xyz")) # Output: xyz
print(minWindow("x", "xy")) # Output: Empty String
print(minWindow("aaabbbccc", "abc")) # Output: aabbc
print(minWindow("aaacbbaac", "abc")) # Output: acb
print(minWindow("aa", "aa")) # Output: aa