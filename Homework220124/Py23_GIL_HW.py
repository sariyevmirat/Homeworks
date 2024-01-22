import random
import threading
import time

def create_file(name):
    time.sleep(1)
    with open(name, 'w'):
        pass

def create_file1():
    start_time = time.time()
    for i in range(5):
        name = f'{i}.txt'
        create_file(name)
    end_time = time.time()
    print(f'Общее время (последовательно): {end_time - start_time}')

def create_file2():
    start_time = time.time()
    threads = []

    def create_file_in_thread(name):
        create_file1(name)

    for i in range(5):
        name = f'{i}.txt'
        thread = threading.Thread(target=create_file_in_thread, args=(name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f'Общее время (многопоточно): {end_time - start_time}')

create_file1()
create_file2()