# a = 0
# while a < 5:
#     a += 1
#     if a == 3:
#         continue
#     print(a)
# for i in range(100):# от 0 до 100 четные числа для for
#     if i % 2 == 0:
#         print(i)
#
# a = 0
# while a <100: # от 0 до 100 четные числа для while
#     if a % 2 == 0:
#         print(a)
#     a += 1
# for i in "hello world": #пробег по строке
#     print(i, end= "-") #end добавляет между буквами символ
# str = "hello world"
# for i in range(len(str)):
#     if i < 2:
#         print(str[i] * 2, end="")
#     else:
#         print(str[i] * 1, end="")
# letter_index = 0
# for i in "hello world":
#     if letter_index < 2:
#         print(i * 2, end = "")
#     else:
#         print(i, end = "")
#     letter_index += 1
# i = 1
# for i in "y", "e", "s":
#     print(i)
# elements = (1, 2, 3, 4)
# for letter in elements:
#     print(letter)
# diapazon = (1, 2, 3, 4, 5)
# for i in diapazon:
#     print(i)

# my_range = range(10, 0, -1)
# for i in my_range:
#     print(i)

str = "hello world"
numbers = [1,2,3,4,5,6]
# for index in range(len(str)):
#     print(index)
#     print(str[index])

# index = 0
for index, letter in enumerate(str):
    # index += 1
    print(index, end = ":")
    print(letter)

