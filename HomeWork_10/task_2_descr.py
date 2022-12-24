"""Second descript"""


class NonMayNegative:
    """Check for negative"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("You input negative number!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Cell:
    """class Cell"""
    quantity = NonMayNegative()

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'Sum of cell = ({self.quantity + other.quantity}).'

    def __sub__(self, other):
        res = self.quantity - other.quantity
        return f"Sub of cell = ({res})." if res > 0 else 'The cell is gone!'

    def __mul__(self, other):
        return f"Multiply of cell = ({self.quantity * other.quantity})."

    def __truediv__(self, other):
        return f"Division of cell = ({self.quantity // other.quantity})."

    def make_order(self, row):
        """make order"""
        result = ''
        for _ in range(int(self.quantity / row)):
            result += '*' * row + '\\n'
        result += '*' * (self.quantity % row)
        return result


print("Create object of cell")
cell1 = Cell(-30)
cell2 = Cell(25)
# cell3 = Cell(10)
# cell4 = Cell(15)
# cell5 = Cell(12)
# print()
# print("Sum")
print(cell1 + cell2)
# print()
# print("Subtraction")
# print(cell2 - cell1)
# print(cell4 - cell3)
# print()
# print("Multiply")
# print(cell2 * cell1)
# print()
# print("Division")
# print(cell1 / cell2)
# print()
# print("Organizing cells by row:")
# print(cell5.make_order(5))
# print(cell2.make_order(10))
