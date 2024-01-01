# #Zadanie №1.
# class Number:
#     def __init__(self, a):
#         self.a = a
#     def __add__(self, b):
#         return Number(self.a + b.a)
#     def __radd__(self, a):
#         return self.__add__(a)
#     def __str__(self):
#         return str(self.a)
# a = Number(10)
# b = Number(12)
# result = a + b
# print(result)
# class Number:
#     def __init__(self, a):
#         self.a = a
#     def __add__(self, b):
#         return Number(self.a + b.a)
#     def __radd__(self, a):
#         return Number(self.a + a)
#     def __str__(self):
#         return str(self.a)
# a = Number(10)
# b = 14 + a
# print(b)

# #Zadaniye №2.
# class Games:
#     Year = 0
#     def __init__(self, year):
#         self.__class__.Year = year
#     def getName(self):
#         pass
# class PCGames(Games):
#     def __init__(self, year, name):
#         super().__init__(year)
#         self.neme = name
#     def getName(self):
#         return self.neme
# class PS4Games(Games):
#     def __init__(self, year, name):
#         super().__init__(year)
#         self.name = name
#     def getName(self):
#         return self.name
# class XboxGames(Games):
#     def __init__(self, year, name):
#         super().__init__(year)
#         self.name = name
#     def getName(self):
#         return self.name
# class MobileGames(Games):
#     def __init__(self, year, name):
#         super().__init__(year)
#         self.name = name
#     def getName(self):
#         return self.name
# pc_game = PCGames(2023, "Lethal company")
# ps4_game = PS4Games(2020, "RDR2")
# xbox_game = XboxGames(2013, "Titanfall")
# mobile_game = MobileGames(2019, "PUBG")
# print(pc_game.getName())
# print(ps4_game.getName())
# print(xbox_game.getName())
# print(mobile_game.getName())

# #Zadanie №3.
# class Country:
#     pass
# class Russia(Country):
#     def __init__(self, population):
#         self.population = population
#     def setPopulation(self):
#         return self.population
#     def getPopulation(self):
#         return self.population
# class Canada(Country):
#     def __init__(self, population):
#         self.population = population
#     def setPopulation(self):
#         return self.population
#     def getPopulation(self):
#         return self.population
# class Germany(Country):
#     def __init__(self, population):
#         self.population = population
#     def setPopulation(self):
#         return self.population
#     def getPopulation(self):
#         return self.population
# russia = Russia(input("Введите популяцию для России: "))
# canada = Canada(input("Введите популяцию для Канады: "))
# germany = Germany(input("Введите популяцию для Германии: "))
# print(russia.getPopulation())
# print(canada.getPopulation())
# print(germany.getPopulation())