#Zadanie 1.
# class Chislo:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self, other):
#         return Chislo(self.x + other.x)
#     def __sub__(self, other):
#         if self.x > other.x:
#             return Chislo(self.x - other.x)
#         else:
#             return Chislo(other.x - self.x)
#     def __mul__(self, other):
#         return Chislo(self.x * other.x)
#     def __truediv__(self, other):
#         if self.x > other.x :
#             return Chislo(self.x / other.x)
#         else:
#             return Chislo(other.x / self.x)
#     def result(self):
#         print(self.x)
# a = Chislo(8)
# b = Chislo(2)
# c = a + b
# c.result()
# c = a - b
# c.result()
# c = a * b
# c.result()
# c = a / b
# c.result()

#Zadanie 2.
# class Drob:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def sokrachenie(self, a, b):
#         while b:
#             a, b = b, a % b
#         return a
#     def __add__(self, other):
#         x1 = self.x * other.y + other.x * self.y
#         x2 = self.y * other.y
#         x3 = self.sokrachenie(x1, x2)
#         return Drob(x1//x3, x2//x3)
#     def __sub__(self, other):
#         if self.x * other.y > other.x * self.y:
#             x1 = self.x * other.y - other.x * self.y
#             x2 = self.y * other.y
#             return Drob(x1, x2)
#         else:
#             x1 = other.x * self.y - self.x * other.y
#             x2 = self.y * other.y
#         x3 = self.sokrachenie(x1, x2)
#         return Drob(x1//x3, x2//x3)
#     def __mul__(self, other):
#         x1 = self.x * other.x
#         x2 = self.y * other.y
#         x3 = self.sokrachenie(x1, x2)
#         return Drob(x1 // x3, x2 // x3)
#     def __truediv__(self, other):
#         x1 = self.x * other.y
#         x2 = self.y * other.x
#         x3 = self.sokrachenie(x1, x2)
#         return Drob(x1//x3, x2//x3)
#     def result(self):
#         print(f'{self.x}/{self.y}')
# a = Drob(5, 8)
# b = Drob(1, 4)
# ab = a + b
# ab.result()
# ab = a - b
# ab.result()
# ab = a * b
# ab.result()
# ab = a / b
# ab.result()

#Zadanie 1.
# import math
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def __eq__(self, other):
#         return self.r == other.r
#     def __gt__(self, other):
#         return self.r > other.r
#     def __lt__(self, other):
#         return self.r < other.r
#     def __ge__(self, other):
#         return self.r >= other.r
#     def __le__(self, other):
#         return self.r <= other.r
#     def __add__(self, other):
#         if isinstance(other, Circle):
#             return Circle(self.r + other.r)
#         else:
#             return Circle(self.r + other)
#     def __sub__(self, other):
#         if isinstance(other, Circle):
#             return Circle(self.r - other.r)
#         else:
#             return Circle(self.r - other)
#     def __iadd__(self, other):
#         self.r += other
#         return self
#     def __isub__(self, other):
#         self.r -= other
#         return self
# circle1 = Circle(5)
# circle2 = Circle(7)
# print(circle1 == circle2)
# print(circle1 < circle2)
# circle3 = circle1 + circle2
# print(circle3.r)
# print((circle1 + 2).r)
# print((circle1 - 3).r)
# circle1 += 3
# print(circle1.r)

#Zadanie 2.
# class Complex:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Complex(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#         return Complex(self.x - other.x, self.y - other.y)
#     def __mul__(self, other):
#         return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
#     def __truediv__(self, other):
#         delenie = other.x ** 2 + other.y ** 2
#         x = (self.x * other.x + self.y * other.y) / delenie
#         y = (self.y * other.x - self.x * other.y) / delenie
#         return Complex(x, y)
#     def __str__(self):
#         return f"({self.x}{' + ' if self.y >= 0 else ' - '}{abs(self.y)}i)"
# x = Complex(2,3)
# y = Complex(-5, -1)
# print(x + y)
# print(x - y)
# print(x * y)
# print(x/y)

#Zadanie 3.
# class Airplane:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#     def __add__(self, other):
#         if isinstance(other, Airplane):
#             return Airplane(self.x + other.x, self.y + other.y)
#         else:
#             return Airplane(self.x + other, self.y + other)
#     def __sub__(self, other):
#         if isinstance(other, Airplane):
#             return Airplane(self.x - other.x, self.y - other.y)
#         else:
#             return Airplane(self.x - other, self.y - other)
#     def __iadd__(self, other):
#             self.x += other
#             self.y += other
#             return self
#     def __isub__(self, other):
#         self.x -= other
#         self.y -= other
#         return self
#     def __gt__(self, other):
#         return self.x > other.x
#     def __lt__(self, other):
#         return self.x < other.x
#     def __ge__(self, other):
#         return self.x >= other.x
#     def __le__(self, other):
#         return self.x <= other.x
# air1 = Airplane(755, 150)
# air2 = Airplane(757, 180)
# print(air1 == air2)
# print(air1 < air2)
# print(air1 > air2)
# air3 = air1 + air2
# air4 = air1 - air2
# print(air3.y)
# print(abs(air4.y))
# print((air1 + 2).y)
# print((air1 - 3).y)
# print((air2 + 2).y)
# print((air2 - 3).y)

#Zadanie 4.
# class Flat:
#     def __init__(self, x, price):
#         self.x = x
#         self.price = price
#
#     def __eq__(self, other):
#         return self.x == other.x
#
#     def __ne__(self, other):
#         return self.x != other.x
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __gt__(self, other):
#         return self.price < other.price
#
#     def __ge__(self, other):
#         return self.price >= other.price
#
#     def __le__(self, other):
#         return self.price <= other.price
#
# flat1 = Flat(100, 20000000)
# flat2 = Flat(150, 25000000)
#
# print(flat1 == flat2)
# print(flat1 > flat2)
# print(flat1 != flat2)
# print(flat1 >= flat2)
# print(flat1 <= flat2)