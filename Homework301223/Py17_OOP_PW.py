#Задание №1.
# class Human:
#     def __init__(self):
#         self.fio = ''
#         self.data = ''
#         self.tel = ''
#         self.city = ''
#         self.country = ''
#         self.adres = ''
#
#     def vvod(self):
#         self.fio = input('Введите ФИО: ')
#         self.data = input('Введите дату рождения: ')
#         self.tel = input('Введите ваш номер телефона: ')
#         self.city = input('Ведите ваш город: ')
#         self.country = input('Введите страну: ')
#         self.adres = input('Введите адрес: ')
#
#     def vivod(self):
#         print('ФИО:',self.fio)
#         print('Дата рождения:', self.data)
#         print('Телефон:', self.tel)
#         print('Город:', self.city)
#         print('Страна:', self.country)
#         print('Адрес:', self.adres)
#
#     def fio_zamena(self):
#         return self.fio
#     def data_zamena(self):
#         return self.data
#     def tel_zamena(self):
#         return self.tel
#     def city_zamena(self):
#         return self.city
#     def country_zamena(self):
#         return self.country
#     def adres_zamena(self):
#         return self.adres
#
# Chelovek = Human()
# Chelovek.vvod()
# print('')
# Chelovek.vivod()
# print('')
# print('ФИО:', Chelovek.fio_zamena())
# print('Дата рождения:', Chelovek.data_zamena())
# print('Телефон', Chelovek.tel_zamena())
# print('Город', Chelovek.city_zamena())
# print('Страна', Chelovek.country_zamena())
# print('Адрес', Chelovek.adres_zamena())

#Задание №2.
# class City:
#     def __init__(self):
#         self.gorod = ''
#         self.region = ''
#         self.strana = ''
#         self.kolichestvo_zhitelei = ''
#         self.index_goroda = ''
#         self.tel_kod = ''
#
#     def vvod(self):
#         self.gorod = input('Введите город: ')
#         self.region = input('Введите регион: ')
#         self.strana = input('Введите страну: ')
#         self.kolichestvo_zhitelei = input('Введите количество жителей: ')
#         self.tel_kod = input('Введите телефонный код города: ')
#
#     def vivod(self):
#         print('город:',self.gorod)
#         print('регио:', self.gorod)
#         print('страна:', self.gorod)
#         print('численность людей:', self.gorod)
#         print('телефонный код города:', self.gorod)
#
#     def a(self):
#         return self.gorod
#     def b(self):
#         return self.region
#
#     def c(self):
#         return self.strana
#
#     def d(self):
#         return self.kolichestvo_zhitelei
#
#     def e(self):
#         return self.tel_kod
#
#
# Dannie_goroda = City()
#
# Dannie_goroda.vvod()
# print('')
# Dannie_goroda.vivod()
# print('')
# print(Dannie_goroda.a())
# print(Dannie_goroda.b())
# print(Dannie_goroda.c())
# print(Dannie_goroda.d())
# print(Dannie_goroda.e())

#Задание №3.
# class Strana:
#     def __init__(self):
#         self.strana = ''
#         self.kontinent = ''
#         self.kolichestvo_zhitelei = ''
#         self.tel_kod = ''
#         self.stolica = ''
#         self.goroda = ''
#
#     def vvod(self):
#         self.strana = input('Введите город: ')
#         self.kontinent = input('Введите регион: ')
#         self.kolichestvo_zhitelei = input('Введите страну: ')
#         self.tel_kod = input('Введите количество жителей: ')
#         self.stolica = input('Введите телефонный код города: ')
#         self.goroda = input('Введите телефонный код города: ')
#
#     def vivod(self):
#         print('Страна:',self.strana)
#         print('Континент:', self.kontinent)
#         print('Количество жителей:', self.kolichestvo_zhitelei)
#         print('телефонный код страны:', self.tel_kod)
#         print('Столица:', self.stolica)
#         print('Города:', self.goroda)
#
#     def a(self):
#         return self.strana
#     def b(self):
#         return self.kontinent
#
#     def c(self):
#         return self.kolichestvo_zhitelei
#
#     def d(self):
#         return self.stolica
#
#     def e(self):
#         return self.goroda
#
#     def f(self):
#         return self.tel_kod
#
#
# Dannie_strani = Strana()
#
# Dannie_strani.vvod()
# print('')
# Dannie_strani.vivod()
# print('')
# print(Dannie_strani.a())
# print(Dannie_strani.b())
# print(Dannie_strani.c())
# print(Dannie_strani.d())
# print(Dannie_strani.e())
# print(Dannie_strani.f())

#Задание №4.
# class Drob:
#     def __init__(self):
#         self.chislitel = ''
#         self.znamenatel = ''
#
#     def vvod(self):
#         self.chislitel = int(input('Введите числитель: '))
#         self.znamenatel = int(input('Введите знаменатель: '))
#
#
#     def vivod(self):
#         print('Числитель:',self.chislitel)
#         print('Знаменатель:', self.znamenatel)
#
#     ravno = '='
#     def a(self):
#         return self.chislitel
#     def b(self):
#         return self.znamenatel
#     def slozhenie(self):
#         resultat = self.znamenatel + self.chislitel
#         return str(self.znamenatel) + ' + ' + str(self.chislitel) + ' = ' + str(resultat)
#     def vichitanie(self):
#         if self.chislitel > self.znamenatel:
#             resultat = self.chislitel - self.znamenatel
#             return str(self.chislitel) + ' - ' + str(self.znamenatel) + ' = ' + str(resultat)
#         else:
#             resultat = self.znamenatel - self.chislitel
#             return str(self.znamenatel) + ' - ' + str(self.chislitel) + ' = ' + str(resultat)
#     def delenie(self):
#         if self.chislitel > self.znamenatel:
#             resultat = self.chislitel / self.znamenatel
#             return str(self.chislitel) + ' / ' + str(self.znamenatel) + ' = ' + str(resultat)
#         else:
#             resultat = self.znamenatel / self.chislitel
#             return str(self.znamenatel) + ' / ' + str(self.chislitel) + ' = ' + str(resultat)
#     def umnozhenie(self):
#         resultat = self.znamenatel * self.chislitel
#         return str(self.znamenatel) + ' * ' + str(self.chislitel) + ' = ' + str(resultat)
# try:
#     ravno = '='
#     Drobi = Drob()
#     Drobi.vvod()
#     print('')
#     Drobi.vivod()
#     print('')
#     print(Drobi.a())
#     print(Drobi.b())
#     print('')
#     print(Drobi.slozhenie())
#     print(Drobi.vichitanie())
#     print(Drobi.delenie())
#     print(Drobi.umnozhenie())
#
# except ValueError:
#     print('Введите целые числа: ')
# except ZeroDivisionError:
#     print('На ноль нельзя делить')

#Задание №5.
# class Python:
#     def __init__(self, name, age, kurs):
#         self.__name = name #private
#         self._age = age #protected
#         self.kurs = kurs #public
#     def set_x(self, name):
#         self.__name = name
#     def get_x(self):
#         return self.__name
#
#
# Student = Python('Мират', 1, 'Разработчик')
# Student.set_x(name='Сариев ')
# Student._age = 27
# Student.kurs = 'Back end Разработчик'
# print(f'{Student._age}, {Student.get_x()}, {Student.kurs}')