# Without using inbuilt function of python: reverse:
# Observe that there are N/2 squares: outer to inner
# We have to rotate each square
# Clockwise rotattion, for anticlockwise change the order of commands

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n//2):
        for j in range(i,n-1-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(rotate(matrix))
print(matrix)