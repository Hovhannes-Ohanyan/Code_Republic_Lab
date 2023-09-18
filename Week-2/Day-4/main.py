# 1
# def max_value(matrix):
#     mv = matrix[0][0]
#     for i in matrix:
#         for j in i:
#             if j > mv:
#                 mv = j
#     return mv
#
#
# matrix = [
#     [1, 2, 3, 4],
#     [6, 7, 8, 9]
# ]
# print(max_value(matrix))

# 2
# def min_value_index(matrix):
#     min_val = matrix[0][0]
#     ind1, ind2 = 0, 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] < min_val:
#                 min_val = matrix[i][j]
#                 ind1, ind2 = i, j
#     return ind1, ind2
#
#
# matrix = [
#     [10, 2, 3, 4],
#     [6, 7, 8, 9]
# ]
# print(min_value_index(matrix))

# 3
# def maxeri_list(matrix):
#     result = []
#     for i in matrix:
#         result.append(max(i))
#     return result
#
#
# matrix = [
#     [10, 2, 3, 4],
#     [6, 7, 8, 9],
#     [1, 2, 3, 4]
# ]
# print(maxeri_list(matrix))


# def sum_main_diagonal_up(matrix):
#     sum = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i < j:
#                 sum += matrix[i][j]
#
#     return sum
#
#
# matrix = [
#     [1, 2, 3, 4],
#     [6, 7, 8, 9],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4]
# ]
#
# print(sum_main_diagonal_up(matrix))

# 5

def sum_secondary_diagonal_down(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i + j > len(matrix) - 1:
                sum += matrix[i][j]
    return sum


matrix = [
    [1, 2, 3, 4],
    [6, 7, 8, 9],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

print(sum_secondary_diagonal_down(matrix))
#



# def odz(matrix):
#     for i in range(len(matrix)):
#         if i % 2 != 0:
#             matrix[i] = matrix[i][::-1]
#     return matrix
#
#
# matrix = [
#     [1, 2, 3, 4],
#     [6, 7, 8, 9],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4]
# ]
#
# print(odz(matrix))


# def foo(matrix):
#     res = []
#     sum = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] % 2 == 0:
#                 sum += matrix[i][j]
#         res.append(sum)
#         sum = 0
#     return res
#
#
# matrix = [
#     [1, 2, 3, 4],
#     [6, 7, 8, 9],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4]
# ]
#
# print(foo(matrix))


# def rec(number):
#     if number < 10:
#         return number
#     last_digit = number % 10
#     number = number // 10
#     return last_digit + rec(number)
#
#
# print(rec(1098))



# def binary_search(lst, start, end, target):
#     if start <= end:
#         mid = (start + end) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             return binary_search(lst, mid + 1, end, target)
#         else:
#             return binary_search(lst, start, mid - 1, target)
#     return -1
#
#
# lst = [1, 2, 3, 4, 5]
# print(binary_search(lst, 0, len(lst) - 1, 5))
