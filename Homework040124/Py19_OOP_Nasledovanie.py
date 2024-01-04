#Zadanie 1.
# class Device:
#     def __init__(self, model, marka):
#         self.model = model
#         self.marka = marka
#
#     def __str__(self):
#         return f'{self.marka}, {self.model}'
# class CoffeeMachine(Device):
#     def __init__(self, model, marka, type):
#         super().__init__(model, marka)
#         self.type = type
#     def __str__(self):
#         return f'{self.marka}, {self.model}, {self.type}'
#     def make_coffe(self):
#         return self.type
# class Blender(Device):
#     def __init__(self, model, marka, speed):
#         super().__init__(model, marka)
#         self.speed = speed
#     def __str__(self):
#         return f'{self.marka}, {self.model}, {self.speed}'
#     def blend(self, item):
#         return f'{item}, {self.speed}'
# class MeatGrinder(Device):
#     def __init__(self, model, marka, meat):
#         super().__init__(model, marka)
#         self.meat = meat
#     def __str__(self):
#         return f'{self.marka}, {self.model}, {self.meat}'
#     def meater(self, farsh):
#         return f'{farsh}, {self.meat}'
# coffemachine = CoffeeMachine('Philips', 'Lattego EP-3241', 'Latte')
# blender = Blender('Kitfort', 'KT-1399', 100000)
# meatgrinder = MeatGrinder('Ardesto','MGL-3580D', 'beef')
# print(coffemachine)
# print(blender)
# print(meatgrinder)

#Zadanie 2.
# class Ship:
#     def __init__(self, type, name):
#         self.type = type
#         self.name = name
#     def __str__(self):
#         return f'{self.type},{self.name}'
# class Frigate(Ship):
#     def __init__(self, type, name, celi):
#         super().__init__(type, name)
#         self.celi = celi
#     def __str__(self):
#         return f'{self.type},{self.celi},{self.name}'
#     def lodka(self):
#         return self.celi
# class Cruiser(Ship):
#     def __init__(self, type, name, progulka):
#         super().__init__(type, name)
#         self.progulka = progulka
#     def __str__(self):
#         return f'{self.type},{self.progulka},{self.name}'
#     def lodka1(self):
#         return self.progulka
# class Destroyer(Ship):
#     def __init__(self, name, type, army):
#         super().__init__(type, name)
#         self.army = army
#     def __str__(self):
#         return f'{self.type},{self.army},{self.name}'
#     def lodka2(self):
#         return self.army
# frigate = Frigate('Яхта ','Адмирал ','Парусная прогулка')
# cruise = Cruiser('Лайнер','Титаник','Круиз')
# destroyer = Destroyer('Ясминец','Линкольн', 'Военный')
# print(frigate)
# print(cruise)
# print(destroyer)

#Zadanie 3.
# class Kolesa:
#     def __init__(self, deistvie):
#         self.deistvie = deistvie
#     def vrachenie(self):
#         return 'Колеса Крутятся'
# class Dvigatel:
#     def __init__(self, deistvie1):
#         self.deistvie1 = deistvie1
#     def rabota(self):
#         return 'Двигатель работает'
# class Dveri:
#     def __init__(self, deistvie2):
#         self.deistvie2 = deistvie2
#     def otkrivanie(self):
#         return 'Двери открываются'
# class Automobile(Kolesa, Dvigatel, Dveri):
#     def __init__(self, deistvie, deistvie1, deistvie2):
#         super().__init__(deistvie)
#         super().__init__(deistvie1)
#         super().__init__(deistvie2)
#     def upravlenie(self):
#         return 'Автомобиль движется'
# my_auto = Automobile(4, '520 HP', 4)
# print(my_auto.upravlenie())
# print(my_auto.vrachenie())
# print(my_auto.rabota())
# print(my_auto.otkrivanie())