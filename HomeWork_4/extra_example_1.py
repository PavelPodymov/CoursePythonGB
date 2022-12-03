"""
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
import math

d = int(input("Inout your precision:\n"))
print(f"d = {d}, Pi = {round(math.pi, d)}")
