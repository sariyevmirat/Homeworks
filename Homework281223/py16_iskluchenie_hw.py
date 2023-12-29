#Задание №1
# class Chess:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
# class Ferz(Chess):
#     def __init__(self, a, b, c, d):
#         super().__init__(a, b, c, d)
#         if not (1 <= a <= 8) or not (1 <= b <= 8) or not (1 <= c <= 8) or not (1 <= d <= 8):
#             print('Вы вышли за границу доски!')
#         elif a == c or b == d or abs(a - c) == abs(b - d):
#             print('YES! Бьет!')
#         else:
#             print('NO! Не бьет!')
#
# class Kon(Chess):
#     def __init__(self, a, b, c, d):
#         super().__init__(a, b, c, d)
#         if not (1 <= a <= 8) or not (1 <= b <= 8) or not (1 <= c <= 8) or not (1 <= d <= 8):
#             print('Вы вышли за границу доски!')
#         elif abs(a - c) == 1 and abs(b - d) == 2 or abs(a - c) == 2 and abs(b - d) == 1:
#             print('YES! Бьет!')
#         else:
#             print('NO! Не бьет!')
# try:
#     a = int(input("Введите номер столбца ферзя: "))
#     b = int(input("Введите номер строки ферзя: "))
#     c = int(input("Введите номер столбца другой клетки ферзя: "))
#     d = int(input("Введите номер строки другой клетки ферзя: "))
#
#     ferz = Ferz(a,b,c,d)
#     kon = Kon(a, b, c, d)
#
# except ValueError:
#     print('Введите число!')

#Задание №2
# def plus_two(x):
#     try:
#         a = 2 + int(x)
#         print(a)
#     except TypeError:
#         print('Ожидаемый тип данных— число!')
#     except ValueError:
#         print("Ожидаемый тип данных— число!")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя")
#
# chislo = input("Введите число: ")
# plus_two(chislo)

#Задание №3
# def massiv(chislo, index):
#     try:
#         a = chislo[index]
#         print(f"Значение элемента с индексом {index}: {a}")
#     except IndexError:
#         print("Ошибка: Индекс выходит за границы массива!")
#
# a = [1,2,3,4,5]
#
# massiv(a,2)
# massiv(a,7)