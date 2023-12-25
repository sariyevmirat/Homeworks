# #1)
# original_list = [-2, -1, 0, 1, 2, 3, 4, 5]
# modified_list = [x ** 3 if x < 0 else x ** 2 for x in original_list if x % 2 == 0]
# print(modified_list)
# #2)
# string_list = ["apple", "banana", "cherry"]
# lengths = [len(s) for s in string_list]
# print(lengths)
# #3)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares_of_evens = [x ** 2 for x in numbers if x % 2 == 0]
# print(squares_of_evens)
# #4)
# numbers = [-10, -7, -5, 0, 3, 6, 9, 15]
# modified_numbers = [x if x > 0 and x % 5 == 0 else 0 for x in numbers]
# print(modified_numbers)
# #5
# my_string = "Hello, World!"
# vowels_only = [char.lower() for char in my_string if char.lower() in "aeiou"]
# print(vowels_only)

#Задание №1.
# def italic_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return f"<i>{result}</i>"
#     return wrapper
# @italic_decorator
# def some_text():
#     return "Это текст, выделенный курсивом."
# italicized_text = some_text()
# print(italicized_text)

#Задание №2.
# def strong_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return f"<strong>{result}</strong>"
#     return wrapper
# @strong_decorator
# def some_text():
#     return "Это ""жирный"" текст."
# strong_text = some_text()
# print(strong_text)

#Задание №3.
# def italic_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return f"<i>{result}</i>"
#     return wrapper
# def strong_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return f"<strong>{result}</strong>"
#     return wrapper
# @strong_decorator
# @italic_decorator
# def some_text():
#     return "Это выделенный курсивом и ""жирный"" текст."
# formatted_text = some_text()
# print(formatted_text)

#Задание №4.