"""
Задание 6.

Создать НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""
from chardet import detect


def encoding_convert(file):
    """encoding"""
    with open(file, 'rb') as file_1:
        f = file_1.read()
    encoding = detect(f)['encoding']
    text = f.decode(encoding)
    print(f'encoding: {encoding}')
    with open('final.txt', 'w', encoding='utf-8') as file_2:
        file_2.write(text)
    return 'final.txt'


# with open(encoding_convert('file_3.txt'), encoding='utf-8') as f_n:
#     for el_str in f_n:
#         print(el_str, end='')

with open(encoding_convert('test_file.txt'), encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
