#1
# def two_list_product():
#     a = [1, 2, 3, 10]
#     b = [1, 2, 3, 3]
#     result = [a[i] * b[i] for i in range(len(a))]
#     return result
#
#
# print(two_list_product())

#2
# def reverse_list(lst: list):
#     return lst[::-1]
# print(reverse_list([1,2,3,4]))

#3
# def arithmetic_average(lst: list):
#     l = len(lst)
#     return sum(lst) / l
# print(arithmetic_average([1,2,3,4]))


#4
# def yes_or_no():
#     n = int(input("Enter Number : "))
#     lst = [1, 2, 3, 4, 5, 6]
#     if n in lst:
#         return "Yes"
#     return "No"
#
#
# print(yes_or_no())

#5
# def string_count(lst: list):
#     d = {}
#     for i in lst:
#         if i in d.keys():
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d
#
#
# print(string_count(["a", "a", "b"]))


#6
# def longest_string(lst: list):
#     max_len = lst[0]
#     max_len_index = 0
#     for i in range(len(lst)):
#         if len(max_len) < len(lst[i]):
#             max_len = lst[i]
#             max_len_index = i
#
#     return (f"longest string : {max_len} \n"
#             f"index longest string : {max_len_index}")
#
#
# print(longest_string(["apple", "banana", "kiwi", "orange", "strawberry"]))


#7
# my_list = ["apple", "banana", "cherry", "date"]
#
# for i in range(len(my_list)):
#     my_list[i] = my_list[i].capitalize()
#
# for item in my_list:
#     print(item[0])


#8
# my_list = ["apple", "banana", "cherry", "date"]
# my_list = [s.lower() for s in my_list]
# my_list.reverse()
# for item in my_list:
#     print(item)


