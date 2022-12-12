from timeit import timeit

from code_4 import fact_list, fact_diction, fact_math

print(timeit("fact_list", globals=globals()))
print(timeit("fact_diction", globals=globals()))
print(timeit("fact_math", globals=globals()))

# отработку функций по памяти и скорости смотри файл code_4.md
