import requests
import json
import random
#a)
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()
with open('phw14_todo.json', 'w') as file:
    json.dump(data, file, indent=2)
print("Файл 'phw14_todo.json' успешно создан.")
#б)
with open('phw14_todo.json', 'r') as file:
    single_todo_data = json.load(file)
print("Данные из файла:")
print(single_todo_data)
#в)
generated_data = []
for _ in range(100):
    todo_dict = {
        'userId': random.randint(1, 10),
        'id': random.randint(101, 200),
        'title': f'Task {random.randint(1, 100)}',
        'completed': random.choice([True, False])
    }
    generated_data.append(todo_dict)
with open('generated_phw14_todos.json', 'w') as file:
    json.dump(generated_data, file, indent=2)
print("Файл 'generated_phw14_todos.json' успешно создан.")