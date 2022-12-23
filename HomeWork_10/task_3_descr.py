"""Third descript"""


class EmptyString:
    """Check for negative"""

    def __set__(self, instance, value):
        if not value or value.isdigit():
            raise ValueError("You input something!")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Stationery:
    """class Stationery"""
    title = EmptyString()

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


stat = Stationery("канцелярская принадлежность")
stat.draw()
stationary = Stationery("0")
stationary.draw()
stationary = Stationery("10")
stationary.draw()
# pen = Pen('ручка')
# pen.draw()
# pencil = Pencil('карандаш')
# pencil.draw()
# handle = Handle('маркер')
# handle.draw()
