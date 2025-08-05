def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    first_row = False
    for i in range(n):
        if matrix[0][i] == 0:
            first_row = True
    first_col = False
    for i in range(m):
        if matrix[i][0] == 0:
            first_col = True
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row:
        for i in range(n):
            matrix[0][i] = 0
    if first_col:
        for i in range(m):
            matrix[i][0] = 0


print(setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # Output: [[1,0,1],[0,0,0],[1,0,1]]
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]