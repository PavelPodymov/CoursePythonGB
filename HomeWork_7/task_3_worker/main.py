"""Information about man"""

from worker import Position

x_man = Position('Pavel', 'Podymov', 'Director', 10, 500)
print(x_man.name)
print(x_man.surname)
print(x_man.position)
# print(x_man._income)
x_man.get_full_name()
x_man.get_total_income()
