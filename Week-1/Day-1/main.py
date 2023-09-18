#1
# def max_value(lst: list):
#     m = lst[0]
#     for i in lst:
#         if i > m:
#             m = i
#     return m
#
#
# print(max_value([1, 2, 3, 4, 5, 6, 7]))
#
#2
# def min_value(lst: list):
#     m = lst[0]
#     for i in lst:
#         if i < m:
#             m = i
#     return m
#
#
# print(min_value([1, 0.5, 2, 3.0, 4, 5.0, 6, 7]))
#
#3
# def max_value_index(lst: list):
#     max_value = lst[0]
#     max_index = 0
#     for i in range(len(lst)):
#         if lst[i] > max_value:
#             max_value = lst[i]
#             max_index = i
#     return max_index
#
#
# print(max_value_index([1, 2, 3, 4, 5, 10111, 1, 3, 6]))
#
#4
# def min_value_index(lst: list):
#     min_value = lst[0]
#     min_index = 0
#     for i in range(len(lst)):
#         if lst[i] < min_value:
#             min_value = lst[i]
#             min_index = i
#     return min_index
#
#
# print(min_value_index([10, 1, 2, 3, 4, 5, 10111, 1, 3, 6]))
#
#5
# def sum_min_max(lst: list):
#     return min(lst) + max(lst)
#
#
# print(sum_min_max([1, 2, 3, 4, 5]))
#
#6
# def sum_and_product(lst: list):
#     sum = 0
#     product = 1
#     for i in lst:
#         sum = sum + i
#         product = product * i
#     return (f"sum of elements : {sum} \n"
#             f"product of elements : {product}")
#
#
# print(sum_and_product([1, 2, 3, 4, 5, 6]))
#
#7
# def index_devide_len(lst: list):
#     l = len(lst)
#     for i in range(l):
#         lst[i] = lst[i] / l
#     return lst
#
#
# print(index_devide_len([1, 2, 3, 4, 5]))
#
#8
# def inp_elements():
#     num = 0
#     result = []
#     size_lst = int(input("please enter size of list : "))
#     while num < size_lst:
#         lst_ints = int(input("Enter the number of elements to add to the list: "))
#         if lst_ints == int(lst_ints):
#             result.append(lst_ints)
#         num += 1
#     return result
#
#
# print(inp_elements())
