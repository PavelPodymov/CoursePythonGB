"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
"""


def get_list(num, start=1):
    """get new list"""
    return list(range(start, num + 1))


def multiply_position(p_list, y_list):
    """multiply el from position in file"""
    result = 1
    for element in p_list:
        try:
            result *= y_list[element]
        except IndexError:
            pass
    return result


with open('file.txt', encoding="utf8") as f:
    string = f.read()
pos_list = [int(string[i]) for i in range(len(string))]
your_num = int(input("Your number: "))
your_list = get_list(your_num)
print(your_list)
print(pos_list)
print(multiply_position(pos_list, your_list))
