# #1
# def fibonacci(n):
#     if n <= 0:
#         return "Invalid input. n must be a positive integer."
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(10))


# 2
# def multiplication_table(num):
#     for i in range(1, 11):
#         result = num * i
#         print(f"{num} x {i} = {result}")
#
#
# num = int(input("Enter a number to generate its multiplication table: "))
# multiplication_table(num)

# 3
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result = result * i
#         return result
#
# print(factorial(7))

# 4
# def sum_digits(n):
#     n = str(n)
#     sum = 0
#     for i in n:
#         sum += int(i)
#     return sum
#
#
# print(sum_digits(1234))


# 5
# def prime(n):
#     if n <= 1:
#         return False
#
#     for i in range(2, int(n ** 0.5 + 1)):
#         if n % i == 0:
#             return False
#         return True
#
# print(prime(11))

# 6
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def can_be_sum_of_primes(n):
#     if n <= 2:
#         return 0
#     for i in range(2, n // 2 + 1):
#         if is_prime(i) and is_prime(n - i):
#             return 1
#
#     return 0
# print(can_be_sum_of_primes(10))


