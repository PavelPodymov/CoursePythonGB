"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать,
вновь выполнить замеры и подготовить аналитику, что вы сделали и чего удалось добиться.

From task 4 HomeWork 5
"""
from googletrans import Translator
from memory_profiler import profile


# First version
@profile()
def fun_1():
    """Use translator from google"""
    translator = Translator()  # забирает памяти 2.0 MiB
    try:
        with open('task_4_file.txt', encoding='utf-8') as data:
            my_list = data.read()

        text_rus = translator.translate(my_list, dest='ru', src='en')  # забирает памяти 1.6 MiB

        with open('task_4_newfile.txt', 'w', encoding='utf-8') as new_file:
            new_file.write(text_rus.text)
    except FileNotFoundError:
        print("You are not created file: 'task_4_file.txt'!")


# Second version
@profile()
def fun_2():
    """use dictionary and if you add new word you need add this word to dict"""
    dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

    try:
        with open('task_4_file.txt', 'r', encoding='UTF8') as file_en:
            text_en = file_en.read()

        text_ru = text_en
        for en_t, ru_t in dictionary.items():
            text_ru = text_ru.replace(en_t, ru_t)

        with open('task_4_new.txt', 'w', encoding='UTF8') as file_ru:
            file_ru.write(text_ru)
    except FileNotFoundError:
        print("You are not created file: 'task_4_file.txt'!")


fun_1()
fun_2()

# Conclusion
# Функция fun_1 по весу больше чем fun_2 за счет использования переводчика
# отработку функций по памяти и скорости смотри файл code_1.md
