"""
For checking
Реализовать функцию int_funcs(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например,
print(int_funcs(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_funcs().
"""


def int_funcs(some_string):
    """ Title """
    return some_string.title()


print(int_funcs("texts"))

print(int_funcs(input("Your strings: ")))

