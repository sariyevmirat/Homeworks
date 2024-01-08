#Zadanie 1.
# class Circle:
#     def __init__(self, dia, h):
#         self.__dia = dia
#         self.__h = h
#         self.__area = self.make_area()
#     def make_area(self):
#         r = self.__dia / 2
#         return 3.14 * r * self.__h
#     @property
#     def area(self):
#         return self.__area
#     def __setattr__(self, key, value):
#         if key == 'dia' or key == 'h':
#             if key == 'dia':
#                 self.__dia = value
#             elif key == 'h':
#                 self.__h = value
#             self.__area = self.make_area()
#         else:
#             super().__setattr__(key, value)
# a = Circle(3, 4)
# print(a.area)
# a.dia = 25
# print(a.area)

#Zadanie 2.
# class Plochad_vigur:
#     __count_calculations = 0
#     @staticmethod
#     def triangle(base, height):
#         Plochad_vigur.__count_calculations += 1
#         return 0.5 * base * height
#     @staticmethod
#     def rectangle(length, width):
#         Plochad_vigur.__count_calculations += 1
#         return length * width
#     @staticmethod
#     def square(side):
#         Plochad_vigur.__count_calculations += 1
#         return side * side
#     @staticmethod
#     def rhombus(diagonal1, diagonal2):
#         Plochad_vigur.__count_calculations += 1
#         return 0.5 * diagonal1 * diagonal2
#     @staticmethod
#     def get_count_calculations():
#         return Plochad_vigur.__count_calculations
#
# area_triangle = Plochad_vigur.triangle(5, 10)
# print(f"Площадь треугольника: {area_triangle}")
#
# area_rectangle = Plochad_vigur.rectangle(4, 10)
# print(f"Площадь прямоугольника: {area_rectangle}")
#
# area_square = Plochad_vigur.square(7)
# print(f"Площадь квадрата: {area_square}")
#
# area_rhombus = Plochad_vigur.rhombus(6, 10)
# print(f"Площадь ромба: {area_rhombus}")
#
# count = Plochad_vigur.get_count_calculations()
# print(f"Количество подсчетов площади: {count}")

#Zadanie 3.
# class MathOperations:
#     @staticmethod
#     def max_of_four(a, b, c, d):
#         return max(a, b, c, d)
#     @staticmethod
#     def min_of_four(a, b, c, d):
#         return min(a, b, c, d)
#     @staticmethod
#     def average_of_four(a, b, c, d):
#         return (a + b + c + d) / 4
#     @staticmethod
#     def factorial(n):
#         if n == 0 or n == 1:
#             return 1
#         else:
#             result = 1
#             for i in range(2, n + 1):
#                 result *= i
#             return result
# a = 5
# b = 6
# c = 7
# d = 8
# max_value = MathOperations.max_of_four(a, b, c, d)
# min_value = MathOperations.min_of_four(a, b, c, d)
# average = MathOperations.average_of_four(a, b, c, d)
# factorial_result_for_a = MathOperations.factorial(a)
# factorial_result_for_b = MathOperations.factorial(b)
# factorial_result_for_c = MathOperations.factorial(c)
# factorial_result_for_d = MathOperations.factorial(d)
#
# print(f"Максимум из четырех: {max_value}")
# print(f"Минимум из четырех: {min_value}")
# print(f"Среднеарифметическое из четырех: {average}")
# print(f"Факториал числа {a}: {factorial_result_for_a}")
# print(f"Факториал числа {b}: {factorial_result_for_b}")
# print(f"Факториал числа {c}: {factorial_result_for_c}")
# print(f"Факториал числа {d}: {factorial_result_for_d}")

#Zadanie 1 Ne smog rewit'