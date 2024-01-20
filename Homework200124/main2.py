import subprocess
import sys
import os
from docx import Document

def setup_virtualenv():
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', 'myenv2'])
        print("Виртуальное окружение создано.")

        activate_script = os.path.join('myenv2', 'Scripts', 'activate')

        subprocess.check_call([activate_script], shell=True)

        subprocess.check_call(['pip', 'install', 'python-docx'])
        print("Библиотека python-docx установлена.")

    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка: {e}")

text_input = input('Введите текст: ')
document = Document()
document.add_paragraph(text_input)

document.save("main2.docx")
input('')