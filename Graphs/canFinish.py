def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    hashmap = {}
    for i in range(numCourses):
        hashmap[i] = []
    for i in prerequisites:
        hashmap[i[0]].append(i[1])
    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if hashmap[course] == []:
            return True
        visited.add(course)
        for i in hashmap[course]:
            if not dfs(i):
                return False
        visited.remove(course)
        hashmap[course] = []
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


print(canFinish(2, [[1,0]])) # Output: True
print(canFinish(2, [[1,0],[0,1]])) # Output: False