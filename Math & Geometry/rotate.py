def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


print(rotate([[1,2,3],[4,5,6],[7,8,9]])) # Output: [[7,4,1],[8,5,2],[9,6,3]]
print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]