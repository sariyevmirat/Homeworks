#Задание №1.
# d = [0]*10
# while True:
#     d[int(input())] += 1
#     if d[0]:
#         break
# print(*d[1:])

#Задание №2.

#Задание №1.
# str_1 = input("text: ")
#
# print(str_1.split(" ")[0])

#Задание №3.
# q1 = [str(i)for i in input("Введите номер телефона: ")]
# q = q1[:]
# q.insert(-2,"-")
# q.insert(-5,"-")
# q.insert(-9,")")
# q.insert(-13,"(")
# if q1[0] == "8":
#     q[0] = "+7"
# if q1[0] == "+" and q1[1] == "8":
#     q.insert(1,"7")
#     q.pop(2)
# print(''.join(map(str,q)))

#Задание №1.
# import random
# M=random.randint(1,10)
# arr=[random.randint(1,10) for i in range(M)]
# for i in range(M):
#     arr[i]=input()
# print(arr)
# print("количество символов в самой длинной строке:" + str(len(max(arr))))
# K=len(max(arr))
# for i in range(M):
#     N=K-len(arr[i])
#     print("*" * N + str(arr[i]))

#Задание №2.
# import random
# import numpy as np
#
# N = int(input("Количество элементов массива"))
# A = [random.randint(-10, 10) for i in range(0, N)]
# print(A)
# Ao = []
# Ap = []
# for i in range(N):
#     if A[i] > 0:
#         Ap.append(A[i])
#     if A[i] < 0:
#         Ao.append(A[i])
# sumAo = np.sum(Ao)
# sumAp = np.sum(Ap)
# sumAo = abs(sumAo)
# Q = (sumAo - sumAp)
#
# print(sumAo)
# print(sumAp)
# print(Q)
#
# if sumAo == sumAp:
#     print("Сумма отрицательных и положительных элементов массива равно")
# if sumAo > sumAp:
#     A.append([Q])
# if sumAp > sumAo:
#     A.append([Q])
#
# print(A)