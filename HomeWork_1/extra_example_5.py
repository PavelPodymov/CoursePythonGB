"""
Напишите программу, которая принимает на вход координаты двух точек и находит
расстояние между ними в 2D пространстве.

Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

coordinate_A = input("Please input coordinate dot A through a space: ")
coordinate_B = input("Please input coordinate dot B through a space: ")
try:
    a_x, a_y = map(float, coordinate_A.split())
    b_x, b_y = map(float, coordinate_B.split())
    result = round((((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5), 2)
    print(f"A ({a_x}; {a_y}); B ({b_x}; {b_y}) -> {result}")
except ValueError:
    print("You write something wrong")
