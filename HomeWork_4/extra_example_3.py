"""
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
"""

lst = list(map(int, input("Input number us space: ").strip().split()))
print(lst)

new_list = [el for el in lst if lst.count(el) == 1]
print(f"Your list is: {new_list}")
