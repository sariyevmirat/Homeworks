import random
import time
from concurrent.futures import ThreadPoolExecutor

def Sozdanie_faila(i):
    start_time = time.time()
    file_name = f'{i+1}.txt'
    time.sleep(1)
    with open(file_name,'w')as text:
        chislo = random.randint(1,100)
        text.write(str(chislo)+'\n')
    end_time = time.time()
    return start_time, end_time

def Cicl():
    start_time = time.time()

    with ThreadPoolExecutor() as executer:
        futures = [executer.submit(Sozdanie_faila, i)for i in range(1000)]
    for futures in futures:
        start, end = futures.result()
        print(f"Файл создан. Время выполнения: {end - start} сек")
    total_time = time.time() - start_time
    print(f"Общее время выполнения для 1000 файлов: {total_time} сек")
Cicl()