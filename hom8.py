# # task 1
#
# def power(base, exponent):
#
#     if exponent == 0:
#         return 1
#
#     else:
#         result = base * power(base, exponent - 1)
#         return result
#
#
# base_value = 2
# exponent_value = 3
# result_power = power(base_value, exponent_value)
# print(f"{base_value}^{exponent_value} = {result_power}")
#
# # task 2
#
# def print_stars(N):
#
#     if N == 0:
#         return
#
#     else:
#         print("*", end="")
#         print_stars(N - 1)
#
#
# user_input = int(input("Enter a number N: "))
# print_stars(user_input)
#
# # task 3
#
# def recursive_sum(a, b):
#
#     if a > b:
#         return 0
#
#     else:
#         return a + recursive_sum(a + 1, b)
#
# a = int(input("Enter the beginning of the range (a): "))
# b = int(input("Enter the end of the range (b): "))

