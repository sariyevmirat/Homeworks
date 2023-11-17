# total_minutes = 0
# total_seconds = 0
# salary = 0
# for hour in range(8):
#     for minute in range(60):
#             salary += 100
        # total_minutes += 1
#         for seconds in range(60):
#             total_seconds += 1
#             if seconds == 30:
#                 break
#
# print(salary)
# print(total_minutes)
# print(total_seconds)

# def helloUser (name):
#     print("Hello, " + name)
#
#
# helloUser("Alt")
# helloUser("Mirat")

# def add(x, y):
#     return x + y

# c = add(2, 3)
# print (c)
#
# print(add(add(2,3), add(4,6)))
#

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# print(factorial(4))

# def max (a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max(3,5))
# print(max(5,3))
# print(max(int(input()), int(input())))


def add(n, m):
    modifier = n + m
    return (n + m) * modifier

def factorial(n):
    # тело функции
    # scope / область видимости
    result = 1
    for i in range(1, n + 1):
        # result = result * i
        result *= i
    return result

modifier = 2

print( factorial(0) )
print( add(2,3) )