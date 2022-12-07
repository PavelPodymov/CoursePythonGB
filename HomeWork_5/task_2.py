"""
1. Создать текстовый файл (не программно), : task_2_file.txt
2. Сохранить в нем несколько строк, : task_2_file.txt
3. выполнить подсчет количества строк, количества слов в каждой строке.
"""
import re

with open('task_2_file.txt', encoding='UTF8') as file:
    s_list = file.readlines()

print(f"Quantity lines = {len(s_list)}")
for i, el in enumerate(s_list, start=1):
    my_el = re.sub(r'[^\w\s]', '', el).split()
    print(f"Line = {i} and quantity words = {len(my_el)}")
    print(*my_el)
