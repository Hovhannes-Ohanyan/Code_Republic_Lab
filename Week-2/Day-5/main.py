
#
#
# def transpose(matrix):
#     for i in range(len(matrix)):
#         for j in range(i + 1, len(matrix)):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#     return matrix
#
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(transpose(matrix))

# def count_adjacent_M(matrix, row, col):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
#     count = 0
#     for dr, dc in directions:
#         r, c = row + dr, col + dc
#         if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == "M":
#             count += 1
#     return count
#
#
# def transform_matrix(matrix):
#     if not matrix:
#         return []
#
#     n = len(matrix)
#     result = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == "M":
#                 result[i][j] = "M"
#             else:
#                 result[i][j] = count_adjacent_M(matrix, i, j)
#     return result
#
#
# matrix = [
#     ['0', 'M', '0', '0', 'M'],
#     ['M', '0', 'M', '0', '0'],
#     ['0', '0', 'M', 'M', 'M'],
#     ['0', '0', '0', '0', '0'],
#     ['0', 'M', '0', 'M', '0']
# ]
# print(transform_matrix(matrix))


# def rotate_180(matrix):
#     result = []
#     for i in range(len(matrix) - 1, -1, -1):
#         result.append(matrix[i][::-1])
#     return result
#
#
# matrix = [
#     [0, 6, 3, 4],
#     [6, 7, 8, 9],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4]
# ]
#
# print(rotate_180(matrix))

#
# def numIslands(matrix):
#     if not matrix or not matrix[0]:
#         return 0
#
#     num_rows = len(matrix)
#     num_cols = len(matrix[0])
#     num_islands = 0
#
#     def sink_island(row, col):
#         if row < 0 or row >= num_rows or col < 0 or col >= num_cols or matrix[row][col] == '0':
#             return
#
#         matrix[row][col] = '0'
#
#         sink_island(row - 1, col)
#         sink_island(row + 1, col)
#         sink_island(row, col - 1)
#         sink_island(row, col + 1)
#
#     for row in range(num_rows):
#         for col in range(num_cols):
#             if matrix[row][col] == '1':
#                 num_islands += 1
#                 sink_island(row, col)
#
#     return num_islands
#
#
# matrix = [
#     ['1', '1', '0', '0', '0'],
#     ['1', '1', '0', '0', '0'],
#     ['0', '0', '1', '0', '0'],
#     ['0', '0', '0', '1', '1']
# ]
#
# print(numIslands(matrix))
