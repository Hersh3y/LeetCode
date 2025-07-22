def foreignDictionary(words: list[str]) -> str:
    result = []
    hashmap = {}
    for i in words:
        for j in i:
            hashmap[j] = set()
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]
        minlen = min(len(word1), len(word2))
        if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
            return ""
        for j in range(minlen):
            if word1[j] != word2[j]:
                hashmap[word1[j]].add(word2[j])
                break
    visited = {}
    
    def dfs(node):
        if node in visited:
            return visited[node]
        visited[node] = True
        for i in hashmap[node]:
            if dfs(i):
                return True
        visited[node] = False
        result.append(node)

    for i in hashmap:
        if dfs(i):
            return ""
    result.reverse()
    return "".join(result)


print(foreignDictionary(["z","o"])) # Output: zo
print(foreignDictionary(["hrn","hrf","er","enn","rfnn"])) # Output: hernf