"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

some_string = input("You string: \n")
my_list = list(some_string.split())
for j, e in enumerate(my_list, 1):
    if len(e) > 10:
        print(j, e[:10])
    else:
        print(j, e)
