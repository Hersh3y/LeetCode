def pacificAtlantic(heights):
    """
    :type heights: List[List[int]]
    :rtype: List[List[int]]
    """
    result = []
    rows = len(heights)
    cols = len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited, prev_height):
        if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or prev_height > heights[r][c]:
            return
        visited.add((r, c))
        dfs(r+1, c, visited, heights[r][c])
        dfs(r-1, c, visited, heights[r][c])
        dfs(r, c+1, visited, heights[r][c])
        dfs(r, c-1, visited, heights[r][c])

    for i in range(cols):
        dfs(0, i, pacific, heights[0][i])
        dfs(rows-1, i, atlantic, heights[rows-1][i])
    for i in range(rows):
        dfs(i, 0, pacific, heights[i][0])
        dfs(i, cols-1, atlantic, heights[i][cols-1])
    for i in range(rows):
        for j in range(cols):
            if (i, j) in pacific and (i, j) in atlantic:
                result.append([i, j])
    return result


print(pacificAtlantic([[1,2,2,3,5],
                       [3,2,3,4,4],
                       [2,4,5,3,1],
                       [6,7,1,4,5],
                       [5,1,1,2,4]])) # Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
print(pacificAtlantic([[1]])) # Output: [[0, 0]]
print(pacificAtlantic([
    [4,2,7,3,4],
    [7,4,6,4,7],
    [6,3,5,3,6]])) # Output: [[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]]
print(pacificAtlantic([[1],
                       [1]])) # Output: [[0, 0], [1, 0]]