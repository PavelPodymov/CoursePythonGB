"""class Stationery"""


class Stationery:
    """class Stationery"""

    def __init__(self, title):
        self.title = title

    def draw(self):
        """draw"""
        print(f'Запуск отрисовки Stationery -> {self.title}')


class Pen(Stationery):
    """class Pen"""

    def draw(self):
        """draw"""
        print(f'Запуск отрисовки Pen -> {self.title}')


class Pencil(Stationery):
    """class Pencil"""

    def draw(self):
        """draw"""
        print(f'Запуск отрисовки Pencil -> {self.title}')


class Handle(Stationery):
    """class Handle"""

    def draw(self):
        """draw"""
        print(f'Запуск отрисовки Handle -> {self.title}')


# stationary = Stationery("канцелярская принадлежность")
# stationary.draw()
# pen = Pen('ручка')
# pen.draw()
# pencil = Pencil('карандаш')
# pencil.draw()
# handle = Handle('маркер')
# handle.draw()
