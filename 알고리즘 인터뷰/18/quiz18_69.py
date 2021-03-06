# 2D 행렬검색 2

# Write an efficient algorithm that searches for a value target
# in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom

# 240
#
# Input: matrix = [[1,4,7,11,15],
#                  [2,5,8,12,19],
#                  [3,6,9,16,22],
#                  [10,13,14,17,24],
#                  [18,21,23,26,30]],
#                 target = 5
# Output: true
#
# Input: matrix = [[1,4,7,11,15]
#                 ,[2,5,8,12,19],
#                  [3,6,9,16,22],
#                  [10,13,14,17,24],
#                  [18,21,23,26,30]], \
#                 target = 20
# Output: false

def search(matrix:list[list[int]],target):
    if not matrix:
        return False
    row, col = 0, len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return True
    return False