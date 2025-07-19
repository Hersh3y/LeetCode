def countComponents(n: int, edges: list[list[int]]) -> int:
    hashmap = {}
    for i in range(n):
        hashmap[i] = []
    for i in edges:
        hashmap[i[0]].append(i[1])
        hashmap[i[1]].append(i[0])
    count = 0
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for i in hashmap[node]:
            dfs(i)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1
    return count


print(countComponents(3, [[0,1], [0,2]])) # Output: 1
print(countComponents(6, [[0,1], [1,2], [2,3], [4,5]])) # Output: 2