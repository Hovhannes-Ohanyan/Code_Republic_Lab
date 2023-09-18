# 1
# def binary_search(lst: list, target):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if lst[mid] == target:
#             return mid
#         if lst[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
# print(binary_search([1, 2, 3, 4, 5, 6], 4))

# 2
# def exp(number,exponent):
#     return number**exponent
# print(exp(10,10))

# 3
# def number_to_string():
#     n=int(input("Write NUmber : "))
#     n=str(n)
#     for i in n:
#         print(f"'{i}'")
# number_to_string()

# 4
# n=int(input("Write integer : "))
# print(hex(n))

# 5
# n=int(input("Write integer : "))
# print(bin(n))

# 6
# l=["1","2","3","4","5"]
# print(l[::-1])

# 7
# def custom_upper(input_string):
#     upper_string = ""
#     for char in input_string:
#         if 'a' <= char <= 'z':
#             upper_string += chr(ord(char) - 32)
#         else:
#             upper_string += char
#     return upper_string
#
#
# input_string = input("Enter a string: ")
# result = custom_upper(input_string)
# print("Uppercase string:", result)
#

# 8
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
# def steps_to_palindrome(initial_number):
#     steps = 0
#     while not is_palindrome(initial_number):
#         inverse_number = int(str(initial_number)[::-1])
#         initial_number += inverse_number
#         steps += 1
#     return steps
#
# initial_number = int(input("Enter an integer: "))
# result = steps_to_palindrome(initial_number)
# print(result)

# # 9
# def find_single_element(arr):
#     left, right = 0, len(arr) - 1
#
#     while left < right:
#         mid = left + (right - left) // 2
#
#         if mid % 2 == 0:
#             if arr[mid] == arr[mid + 1]:
#                 left = mid + 2
#             else:
#                 right = mid
#
#         else:
#             if arr[mid] == arr[mid - 1]:
#                 left = mid + 1
#             else:
#                 right = mid
#
#     return arr[left]
#
#
# arr = [1, 1, 2, 2, 3, 3, 4, 4, 5]
# single_element = find_single_element(arr)
# print(single_element)
