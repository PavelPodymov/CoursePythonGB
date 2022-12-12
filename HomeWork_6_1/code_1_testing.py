"""Testing code"""
from timeit import timeit

print(timeit("fun_1", globals=globals()))
print(timeit("fun_2", globals=globals()))

#
# скорость fun_1 = 0.028512899996712804 приблизительно
# скорость fun_2 = 0.04571970005054027 приблизительно

# Conclusion
# при использовании библиотеки googletrans код получается тяжелее, но быстрее!
# отработку функций по памяти и скорости смотри файл code_1.md
