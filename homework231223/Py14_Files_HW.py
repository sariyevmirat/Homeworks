import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos/')
data = response.json()

with open('hw14_data.json', 'w') as file:
    json.dump(data, file, indent=2)

print("Файл 'hw14_data.json' успешно создан.")

with open('hw14_data.json', 'r') as file:
    todos_array = json.load(file)

print("Данные из файла:")
print(todos_array)

for i, todo_dict in enumerate(todos_array, start=1):
    filename = f'todo_{i}.json'
    with open(filename, 'w') as file:
        json.dump(todo_dict, file, indent=2)
    print(f"Файл '{filename}' успешно создан.")

    with open(filename, 'r') as file_read:
        content = json.load(file_read)
        print(f"Содержимое файла '{filename}':")
        print(content)