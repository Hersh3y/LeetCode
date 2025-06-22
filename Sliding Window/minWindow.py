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


print(minWindow("ADOBECODEBANC", "ABC")) # Outputs BANC
print(minWindow("a", "a")) # Outputs a
print(minWindow("a", "aa")) # Outputs Empty String
print(minWindow("OUZODYXAZV", "XYZ")) # Outputs YXAZ
print(minWindow("xyz", "xyz")) # Outputs xyz
print(minWindow("x", "xy")) # Outputs Empty String
print(minWindow("aaabbbccc", "abc")) # Outputs aabbc
print(minWindow("aaacbbaac", "abc")) # Outputs acb
print(minWindow("aa", "aa")) # Outputs aa