"""
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""


def get_list(end, start=1):
    """get new list"""
    return list(range(start, end + 1))


len_list = int(input("Your number: "))
your_list = get_list(len_list)
print(your_list)

for i in range(0, len(your_list), 2):
    try:
        your_list[i], your_list[i + 1] = your_list[i + 1], your_list[i]
    except IndexError:
        pass
print(your_list)
