# 1
# def print_numbers_reverse(n):
#     if n >= 0:
#         print(n)
#         if n > 0:
#             print_numbers_reverse(n - 1)
#     else:
#         return
#
#
# print_numbers(5)
#
# 2
# def print_numbers(n):
#     if n >= 0:
#         if n > 0:
#             print_numbers(n - 1)
#         print(n)
#
#
# print_numbers(9)
#
#3
# def print_list_elements(lst: list, index=0):
#     if index < len(lst):
#         print(lst[index])
#         print_list_elements(lst, index + 1)
#
# print_list_elements([1, 2, 3, 4, 5])
#

#4
# def sum_of_digits(number):
#     if number < 10:
#         return number
#     else:
#         return number % 10 + sum_of_digits(number // 10)
#
#
# print(sum_of_digits(12345))
