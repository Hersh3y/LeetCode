def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    hashmap = {}
    for i in range(len(strs)):
        anagram_sorted = "".join(sorted(strs[i]))
        if anagram_sorted not in hashmap:
            hashmap[anagram_sorted] = []
        hashmap[anagram_sorted].append(strs[i])
    return hashmap.values()


groupAnagrams(["eat","tea","tan","ate","nat","bat"]) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
groupAnagrams([""]) # Output: [[""]]
groupAnagrams(["a"]) # Output: [["a"]]