def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    hashmap = {len(s):1}
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            hashmap[i] = 0
        else:
            hashmap[i] = hashmap[i+1]
        if len(s) > i + 1 and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
            hashmap[i] += hashmap[i+2]
    return hashmap[0]


print(numDecodings("12")) # Output: 2
print(numDecodings("226")) # Output: 3
print(numDecodings("06")) # Output: 0