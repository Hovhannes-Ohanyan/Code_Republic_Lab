# 1
# def odd_count(lst: list):
#     count = 0
#     for i in lst:
#         if i % 2 != 0:
#             count += 1
#     return count
#
#
# print(odd_count([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 2
# char_array = []
#
# while True:
#     char = input("write strings : ")
#     if char == "done":
#         break
#     char_array.append(char)
#
# uppercase_string = ''.join(char_array).upper()
#
# print("Upper :", uppercase_string)


# 3
# def reverse_char_list(lst:list):
#     return lst[::-1]
#
# print(reverse_char_list(["apple", "banana", "kiwi", "orange", "strawberry"]))


# 4
# char_array = []
#
# while True:
#     char = input("write integers : ")
#     if char == "done":
#         break
#     char_array.append(char)
# max_value_index=char_array.index(max(char_array))
# min_value_index=char_array.index(min(char_array))
# print(max_value_index-min_value_index)


# 5

# def first_evens_second_odds(lst:list):
#     for i in lst:
#         if i%2==1:
#             lst.append(i)
#             lst.remove(i)
#     return lst
# print(first_evens_second_odds([1,2,3,4,5,6]))


# 6
# lst1 = [1, 2, 3, 4]
# lst2 = [1, 2, 3, 5]
# equal = True
# for i in range(len(lst1)):
#     if lst1[i] != lst2[i]:
#         equal = False
#         break
# if equal:
#     print("all values are the same both lists")
# else:
#     print("not all values are the same both lists")

