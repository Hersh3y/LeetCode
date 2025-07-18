def validTree(n: int, edges: list[list[int]]) -> bool:
    hashmap = {}
    for i in range(n):
        hashmap[i] = []
    for i in edges:
        hashmap[i[0]].append(i[1])
        hashmap[i[1]].append(i[0])
    visited = set()
    
    def dfs(node, prev):
        if node in visited:
            return False
        visited.add(node)
        for i in hashmap[node]:
            if i == prev:
                continue
            if not dfs(i, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n



print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])) # Output: True
print(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])) # Output: False