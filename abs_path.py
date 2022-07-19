import os

# Функция возвращает абсолютный путь к файлу, где исполнялся скрипт
current_directory = os.path.dirname(os.path.abspath(__file__))

print(current_directory)