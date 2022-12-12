"""find max number"""
from timeit import timeit

print(timeit("max_number", globals=globals()))
print(timeit("max_number_2", globals=globals()))
print(timeit("max_number_3", globals=globals()))

# max_number
# 0.01223510003183037
# max_number_2
# 0.015995200024917722
# max_number_3
# 0.023888999945484102

# Generator expression, работает медленнее
# отработку функций по памяти и скорости смотри файл code_2.md
