# 1

# def fibonaci(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     if n==3:
#         return 1
#     if n>2:
#         return fibonaci(n-1)+fibonaci(n-2)
# print(fibonaci(15))

# 2


# def factorial(n):
#     if n==0:
#         return 1
#     if n==1:
#         return 1
#     if n>1:
#         return n*factorial(n-1)
# print(factorial(6))
#
# def binary_search(lst: list, low, high, target):
#     if low <= high:
#         mid = (low + high) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             return binary_search(lst, mid + 1, high, target)
#         else:
#             return binary_search(lst, low, mid - 1, target)
#     return -1
#
#
# lst = [1, 2, 3, 4, 5, ]
# target = 5
# print(binary_search([1, 2, 3, 4, 5, 6, 7], 0, len(lst) - 1, target))
# def odds_and_evens(lst):
#     even_index = 0
#     odd_index = len(lst) - 1
#
#     while even_index < odd_index:
#         if lst[even_index] % 2 == 0:
#             even_index += 1
#         else:
#             lst[even_index], lst[odd_index] = lst[odd_index], lst[even_index]
#             odd_index -= 1
#
#     return lst
#
# odds_and_evens([1,2,3,4,5,6,7,8])
