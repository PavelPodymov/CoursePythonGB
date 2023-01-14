"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
list_of_w = ['разработка', 'администрирование', 'protocol', 'standard']

for i in list_of_w:
    ENC_W = i.encode('utf-8')
    DEC_W = ENC_W.decode('utf-8')
    print(i, ENC_W, DEC_W)
    print(type(i), type(ENC_W), type(DEC_W))
    print()
