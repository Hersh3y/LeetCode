def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    hashmap = {}
    for i in s:
        if i not in hashmap:
            hashmap[i] = 0
        hashmap[i] += 1
    for i in t:
        if i not in hashmap:
            return False
        hashmap[i] -= 1
        if hashmap[i] < 0:
            return False
    return True


print(isAnagram("anagram", "nagaram")) # Outputs True
print(isAnagram("rat", "car")) # Outputs False