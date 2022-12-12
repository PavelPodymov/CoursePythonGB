Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    14     31.7 MiB     31.7 MiB           1   @profile()
    15                                         def fun_1():
    16                                             """Use translator from google"""
    17     33.7 MiB      2.1 MiB           1       translator = Translator()  # забирает памяти 2.0 MiB
    18     33.7 MiB      0.0 MiB           1       try:
    19     33.7 MiB      0.0 MiB           2           with open('task_4_file.txt', encoding='utf-8') as data:
    20     33.7 MiB      0.0 MiB           1               my_list = data.read()
    21                                         
    22     35.3 MiB      1.6 MiB           1           text_rus = translator.translate(my_list, dest='ru', src='en')  # забирает памяти 1.6 MiB
    23                                         
    24     35.3 MiB      0.0 MiB           2           with open('task_4_newfile.txt', 'w', encoding='utf-8') as new_file:
    25     35.3 MiB      0.0 MiB           1               new_file.write(text_rus.text)
    26                                             except FileNotFoundError:
    27                                                 print("You are not created file: 'task_4_file.txt'!")


Filename: D:\GeekBrains\Python\CoursePythonGB\HomeWork_6\code_1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    31     34.8 MiB     34.8 MiB           1   @profile()
    32                                         def fun_2():
    33                                             """use dictionary and if you add new word you need add this word to dict"""
    34     34.8 MiB      0.0 MiB           1       dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    35                                         
    36     34.8 MiB      0.0 MiB           1       try:
    37     34.8 MiB      0.0 MiB           2           with open('task_4_file.txt', 'r', encoding='UTF8') as file_en:
    38     34.8 MiB      0.0 MiB           1               text_en = file_en.read()
    39                                         
    40     34.8 MiB      0.0 MiB           1           text_ru = text_en
    41     34.9 MiB      0.0 MiB           5           for en_t, ru_t in dictionary.items():
    42     34.9 MiB      0.0 MiB           4               text_ru = text_ru.replace(en_t, ru_t)
    43                                         
    44     34.9 MiB      0.1 MiB           2           with open('task_4_new.txt', 'w', encoding='UTF8') as file_ru:
    45     34.9 MiB      0.0 MiB           1               file_ru.write(text_ru)
    46                                             except FileNotFoundError:
    47                                                 print("You are not created file: 'task_4_file.txt'!")


def fun_1() 0.029779899981804192
def fun_2() 0.06192500004544854

Process finished with exit code 0