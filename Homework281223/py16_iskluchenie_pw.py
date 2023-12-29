#Задание №1
# a = input("Введите а: ")
# b = input("Введите b: ")
#
# try:
#     summ = float(a)+float(b)
#     print(summ)
# except ValueError:
#     print(a+b)

#Задание №2
# a = input("введите трехзначное число: ")
# try:
#     dlinna = list(map(int, a))
#     if len(dlinna) != 3:
#         print("Число должно быть трехзначное!")
#     else:
#         b = sum(int(i) for i in str(a))
#         print(b)
# except ValueError:
#     print(" You can’t divide on zero")
# except ZeroDivisionError:
#     print(" You can’t divide on zero")
#
# #Задание №3
# class Pole:
#     def __init__(self):
#         pass
#
#     def check_pole(self, a, b, c, d):
#         if not (1 <= a <= 8) or not (1 <= b <= 8) or not (1 <= c <= 8) or not (1 <= d <= 8):
#             print("Вы вышли за границу доски!")
#
#     def sravnenie (self,a,b,c,d):
#         if (a + b) % 2 == (c + d) % 2:
#             print('YES')
#         else:
#             print('NO')
#     def check_ladya(self, aa, bb, cc, dd):
#         if ((aa == cc) or (bb == dd)):
#             print('YES! Бьет!')
#         else:
#             print('NO! не бьет')
# try:
#     pole = Pole()
#     a = int(input("Введите номер столбца короля: "))
#     b = int(input("Введите номер строки короля: "))
#     c = int(input("Введите номер столбца другой клетки: "))
#     d = int(input("Введите номер строки другой клетки: "))
#
#     pole.check_pole(a, b, c, d)
#     pole.sravnenie(a, b, c, d)
#
#     pole2 = Pole()
#     aa = int(input("Введите номер столбца короля : "))
#     bb = int(input("Введите номер строки короля: "))
#     cc = int(input("Введите номер столбца другой клетки: "))
#     dd = int(input("Введите номер строки другой клетки: "))
#
#     pole2.check_ladya(aa, bb, cc, dd)
#     pole2.check_pole(aa, bb, cc, dd)
#
#
# except ValueError:
#     print('Введите число!')
#
# #Задание №4
# class Ladya:
#     def __init__(self):
#         pass
#
#     def check_pole(self, a, b, c, d):
#         if not (1 <= a <= 8) or not (1 <= b <= 8) or not (1 <= c <= 8) or not (1 <= d <= 8):
#             print("Вы вышли за границу доски!")
#             return
#
#         if ((a + 1 == c) or (a - 1 == c) or (a == c)) and ((b == d) or (b + 1 == d) or (b - 1 == d)):
#             print('YES!')
#         else:
#             print('NO!')
#
# try:
#     pole = Ladya()
#     a = int(input("Введите номер столбца короля: "))
#     b = int(input("Введите номер строки короля: "))
#     c = int(input("Введите номер столбца другой клетки: "))
#     d = int(input("Введите номер строки другой клетки: "))
#
#     pole.check_pole(a, b, c, d)
#
# except ValueError:
#     print('Введите число!')

#Задание №5
# from inspect import Traceback
#
# def avg(a, b):
#     return (a * b) ** 0.5
#
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#
#     if a == 0 or b == 0:
#         raise ValueError("только не ноль")
#
#     c = avg(a, b)
#     print("Среднее геометрическое = {:.2f}".format(c))
#
# except ValueError:
#     print("Вводи цифры")
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль")
# except Exception as e:
#     print(f"Произошла непредвиденная ошибка: {e}")
#
# #Задание №6
# class RomanConverter:
#     def __init__(self):
#         self.roman_numerals = {
#             0: '0', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
#             6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
#             20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
#             60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 1000: 'M',
#             2000: 'MM', 3000: 'MMM', 4000: 'MMMM', 5000: 'MMMMM', 6000: 'MMMMMM',
#             7000: 'MMMMMMM', 8000: 'MMMMMMMM', 9000: 'MMMMMMMMM', 10000: 'MMMMMMMMMM'
#             }
#
#     def to_roman(self, number):
#         if number in self.roman_numerals:
#             return self.roman_numerals[number]
#         else:
#             blizhnii = max(key for key in self.roman_numerals if key <= number)
#             remainder = number - blizhnii
#             return self.roman_numerals[blizhnii] + self.to_roman(remainder)
#
#
# class Calculator:
#     def __init__(self):
#         self.converter = RomanConverter()
#
#     def add(self, a, b):
#         roman_a = self.converter.to_roman(a)
#         roman_b = self.converter.to_roman(b)
#
#         result = a + b
#         result1 = a * b
#         result2 = max(a, b) / min(a, b)
#         result3 = max(a, b) - min(a, b)
#
#         roman_result = self.converter.to_roman(result)
#         roman_result1 = self.converter.to_roman(result1)
#         roman_result2 = self.converter.to_roman(int(result2))
#         roman_result3 = self.converter.to_roman(int(result3))
#
#         print(f'{roman_a} + {roman_b} = {roman_result}')
#         print(f'{roman_a} * {roman_b} = {roman_result1}')
#         print(f'{roman_a} / {roman_b} = {roman_result2}')
#         print(f'{roman_a} - {roman_b} = {roman_result3}')
#
# try:
#     calc = Calculator()
#
#
#     a = int(input("Введите первое значение: "))
#     b = int(input("Введите второе значение: "))
#
#     calc.add(a, b)
#
# except ValueError:
#     print("Введите числа: ")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль: ")
#
# #Задание №7
# class NameTooLongError(Exception):
#     pass
#
# def check_name(name):
#     if len(name) > 4:
#         raise NameTooLongError("Имя длиннее четырех символов!")
#
#
# try:
#     name = input("Введите имя: ")
#     check_name(name)
#     print("Имя подходит")
# except NameTooLongError as j:
#     print(j)
#

#Задание №8
# class InvalidInputError(Exception):
#     pass
#
# class Deposit:
#     def __init__(self, principal, interest_rate, time):
#         self.principal = principal
#         self.interest_rate = interest_rate
#         self.time = time
#
#     def calculate_simple_interest(self):
#         return self.principal * self.interest_rate * self.time
#
#     def calculate_capitalized_interest(self, times_compounded):
#         return self.principal * ((1 + self.interest_rate / times_compounded) ** (times_compounded * self.time))
#
# def select_deposit_type():
#     print("Выберите тип вклада:")
#     print("1. Срочный вклад")
#     print("2. Бонусный вклад")
#     print("3. Вклад с капитализацией процентов")
#     choice = int(input("Введите номер: "))
#     return choice
#
# def main():
#     try:
#         principal = float(input("Введите начальную сумму вклада: "))
#         interest_rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
#         time = float(input("Введите срок вклада (в годах): "))
#
#         deposit_type = select_deposit_type()
#
#         if deposit_type == 1:
#             deposit = Deposit(principal, interest_rate, time)
#             interest = deposit.calculate_simple_interest()
#             print(f"Прибыль по срочному вкладу: {interest}")
#
#         elif deposit_type == 2:  # Бонусный вклад
#             bonus_threshold = 1000
#             if principal >= bonus_threshold:
#                 deposit = Deposit(principal, interest_rate, time)
#                 interest = deposit.calculate_simple_interest()
#                 bonus = interest * interest_rate
#                 print(f"Прибыль по бонусному вкладу: {interest}")
#                 print(f"Бонус: {bonus}")
#             else:
#                 print("Сумма вклада ниже минимальной для начисления бонуса")
#
#         elif deposit_type == 3:
#             times_compounded = int(input("Введите количество раз, когда проценты капитализируются за год: "))
#             deposit = Deposit(principal, interest_rate, time)
#             interest = deposit.calculate_capitalized_interest(times_compounded)
#             print(f"Прибыль по вкладу с капитализацией процентов: {interest}")
#
#         else:
#             raise InvalidInputError("Неверный выбор типа вклада")
#
#     except ValueError:
#         print("Ошибка ввода. Введите числовое значение.")
#     except ZeroDivisionError:
#         print("Ошибка: деление на ноль")
#     except InvalidInputError as e:
#         print(e)
#
# if __name__ == "__main__":
#     main()