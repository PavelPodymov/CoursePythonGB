"""
For checking
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

import math

my_lst = list(map(int, input("Input your numbers: ").strip().split()))
lngth = len(my_lst)
new_lst = [my_lst[i] * my_lst[lngth - i - 1] for i in
           range(math.ceil(lngth / 2))]
print(new_lst)
