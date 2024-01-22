import random
import time
import threading


def Slozhenie1():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    time.sleep(1)
    print(f"Результат сложения {a} + {b} = {a+b}")

def Slozhenie2():
    start_time = time.time()
    for i in range(5):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        time.sleep(1)
        end_time = time.time()
        print(f"Результат сложения {a} + {b} = {a + b} Затраченное время на решение {end_time-start_time}")
    print(f"Общее время: {end_time - start_time}")

def Slozhenie3():
    start_time = time.time()
    threads = []

    for i in [Slozhenie1, Slozhenie2]:
        thread = threading.Thread(target=i)
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()

    end_time = time.time()
    print(f"Многопоточный режим: {end_time - start_time}")


Input = int(input("Запустить цикл сложения? 1 [Да] - 2 [Нет]: "))
if Input == 1:
    Slozhenie1()
    Slozhenie2()
    Slozhenie3()
else:
    print('Цикл не запущен')