"""Power"""
from timeit import timeit
from code_3 import my_func_1, my_func_21

print(timeit("my_func_1", globals=globals()))
print(timeit("my_func_21", globals=globals()))

# Функция my_func_1 быстрее my_func_21
# отработку функций по памяти и скорости смотри файл code_3.md
