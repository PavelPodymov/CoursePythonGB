"""
Задание 1
Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


def get_info(some_list):
    """print info"""
    for i in some_list:
        print(f'word: {i} -> type: {type(i)}')
    print()


list_of_w = ['разработка', 'сокет', 'декоратор']

for i in list_of_w:
    print(ascii(i))

print()

list_unc_w = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
              '\u0441\u043e\u043a\u0435\u0442',
              '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

get_info(list_of_w)
get_info(list_unc_w)
