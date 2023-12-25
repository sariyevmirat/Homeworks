#1)
# def generator_1(input_list):
#     return {x: x**3 for x in input_list if x % 2 != 0}
# input_list_1 = [1, 2, 3, 4, 5, 6, 7]
# result_1 = generator_1(input_list_1)
# print(result_1)
# #2)
# def generator_2(input_list):
#     return {x for x in input_list if x % 2 == 0}
# input_list_2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# result_2 = generator_2(input_list_2)
# print(result_2)
#3)
# def generator_3():
#     return [i * 10 for i in range(10)]
# result_3 = generator_3()
# print(result_3)
#4)
# def divisor_generator(n):
#     for i in range(n + 1):
#         if i % 7 == 0:
#             yield i
# result_4 = list(divisor_generator(100))
# print(result_4)

#Задание 5.
# import re
# from itertools import permutations
# def generate_words(input_str):
#     filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)
#     words = set()
#     for r in range(1, len(filtered_str) + 1):
#         perms = permutations(filtered_str, r)
#         for perm in perms:
#             word = ''.join(perm)
#             words.add(word)
#     sorted_words = sorted(words, key=lambda x: (not x.isdigit(), len(x), x))
#     for w in sorted_words:
#         print(w)
#     print(len(sorted_words))
# input_str = "k98.ok"
# generate_words(input_str)