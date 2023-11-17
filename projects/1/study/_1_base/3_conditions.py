# TODO условный оператор if-else

bool1 = True

#   True
if bool1:
    print("Правда 1")

#   True
if bool1:
    print("Правда 1")
# False
else:
    print("Правда 2")

value = 40

if value > 50:
    print("Правда 3")
else:
    print("Правда 4")

if value > 50:
    print("Правда 3")
else:
    if value > 45:
        print("Правда 4")
    else:
        print("Правда 5")

if value > 50:
    print("Правда 3")
elif value > 45:
    print("Правда 4")
else:
    print("Правда 5")


fruit = "апельсин"
if fruit == "абрикос":
    print("У Вас аллергия, будьте осторожны")
# elif fruit == "банан":
# elif fruit in ["банан", 'яблоко']:
#         False                True
# elif fruit in "банан" and fruit in "яблоко":
#        True                   False
# elif fruit in "банан" or fruit in "яблоко":
#                      True                           False
#             True            False
elif (fruit in "банан" or fruit in "яблоко") and fruit in "апельсин":
    print("Всё в норме")
else:
    print("Неизвестный фрукт")


fruit = "апельсин"
if fruit == "абрикос":
    print("У Вас аллергия, будьте осторожны")
elif fruit in "банан":
    print("Всё в норме")
elif fruit in "яблоко":
    print("Всё супер")
else:
    print("Неизвестный фрукт")

match fruit:
    case "абрикос":
        print("У Вас аллергия, будьте осторожны")
    case "банан":
        print("Всё в норме")
    case "яблоко":
        print("Всё супер")
    case _:
        print("Неизвестный фрукт")

light = 'Жёлтый'

match light:
    case "Зеленый":
        print("Старт")
    case "Жёлтый":
        print('Внимание')
    case 'Красный':
        print('STOP!')
    case _:
        print('Светофор не работает')

# a = 17

# print(a == 17)
# print(a != 17)
# cond1 = a is 17.0
# cond2 = a is not 17
# print(cond2)


