"""First descript"""


class NonMayNegative:
    """Check for negative"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("You input negative number!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    """class Road"""
    length = NonMayNegative()
    width = NonMayNegative()

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 0.025
        self.height = 5

    def mass_asphalt(self):
        """Calculate mass of asphalt"""
        mass = self.length * self.width * self.weight * self.height
        print(f"Mass of asphalt you need for 1 cubic meter = {mass:.0f} t")


r = Road(10, 5000)
r.mass_asphalt()

r.length = -20
r.width = 5000
r.mass_asphalt()
