"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов не используя!!! методы encode и decode
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции.
"""


def get_info(some_list):
    """print info"""
    for i in some_list:
        print(f'word: {i} -> type: {type(i)} -> length: {len(i)}')
    print()


list_of_w = ['class', 'function', 'method']
list_b_w = [b'class', b'function', b'method']
get_info(list_of_w)
get_info(list_b_w)
