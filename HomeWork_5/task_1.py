"""
1. Создать программно файл в текстовом формате,
2. записать в него построчно данные, вводимые пользователем.
3. Об окончании ввода данных свидетельствует пустая строка.
"""
with open('file_1.txt', "w", encoding='utf-8') as file:
    START = True
    while START:
        line = input()
        file.write(line + '\n')
        if not line:
            START = False
