"""Class ROAD"""


class Road:
    """class Road"""

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 0.025
        self.height = 5

    def mass_asphalt(self):
        """Calculate mass of asphalt"""
        mass = self._length * self._width * self.weight * self.height
        print(f"Mass of asphalt you need for 1 cubic meter = {mass:.0f} t")


# r = Road(10, 5000)
# r.mass_asphalt()
