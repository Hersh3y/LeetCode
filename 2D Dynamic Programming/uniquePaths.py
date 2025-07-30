def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    table = []
    for i in range(m):
        table.append([1] * n)
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[m-1][n-1]


print(uniquePaths(3, 7)) # Output: 28
print(uniquePaths(3, 2)) # Output: 3
print(uniquePaths(3, 6)) # Output: 21
print(uniquePaths(3, 3)) # Output: 6