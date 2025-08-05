def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    l = 0
    r = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1
    while r >= l and bottom >= top:
        for i in range(l, r + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][r])
        r -= 1
        if bottom >= top:
            for i in range(r, l - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if r >= l:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][l])
            l += 1
    return result


print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # Output: [1,2,3,6,9,8,7,4,5]
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # Output: [1,2,3,4,8,12,11,10,9,5,6,7]