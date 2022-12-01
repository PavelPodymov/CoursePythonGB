"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
import math

my_list = list(map(int, input("Input your numbers: ").strip().split()))
leng = len(my_list)
new_list = [my_list[i] * my_list[leng - i - 1] for i in
            range(math.ceil(leng / 2))]
print(new_list)