"""
1. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
task_4_file.txt
2. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from googletrans import Translator

translator = Translator()

try:
    with open('task_4_file.txt', encoding='utf-8') as data:
        my_list = data.read()

    text_rus = translator.translate(my_list, dest='ru', src='en')

    with open('task_4_newfile.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(text_rus.text)
except FileNotFoundError:
    print("You are not created file: 'task_4_file.txt'!")


# Second version
dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

try:
    with open('task_4_file.txt', 'r', encoding='UTF8') as file_en:
        text_en = file_en.read()

    text_ru = text_en
    for en, ru in dictionary.items():
        text_ru = text_ru.replace(en, ru)

    with open('task_4_new.txt', 'w', encoding='UTF8') as file_ru:
        file_ru.write(text_ru)
except FileNotFoundError:
    print("You are not created file: 'task_4_file.txt'!")
