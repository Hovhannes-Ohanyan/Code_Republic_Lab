# 1
# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for i in m:
#     for j in i:
#         print(j)

# 2
# def sum_ankyunagit(m):
#     sum = 0
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             if i == j:
#                 sum += m[i][j]
#     return sum
#
#
# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(sum_ankyunagit(m))

# 3
# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for i in range(len(m)):
#     if i % 2 == 0:
#         for j in range(len(m[i])):
#             m[i][j] = 0
# print(m)


# 4
# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# n = len(m)
# sum = 0
# for i in range(n):
#     sum += m[i][n - 1 - i]
# print(sum)

# 5

# def ankyunagtiic_verev_sum(m):
#     sum=0
#     for i in range(len(m)):
#         for j in range(i,len(m)):
#             sum+=m[i][j]
#     return sum
# print(ankyunagtiic_verev_sum([[1,2,3],[4,5,6],[7,8,9]]))


#6
# def change_elements(m):
#     n = len(m)
#     for i in range(n):
#         m[i][i], m[i][n - 1 - i] = m[i][n - 1 - i], m[i][i]
#     return m
#
#
# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(change_elements(m))

