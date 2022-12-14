"""Class Worker"""


class Worker:
    """Class Worker"""

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    """get info about man"""

    # def __init__(self, name, surname, position, wage, bonus):
    #     super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        """get full name"""
        print(f"Your name: {self.name} {self.surname}\nYou are: {self.position}")

    def get_total_income(self):
        """get total income"""
        res = self._income['wage'] + self._income['bonus']
        print(f"Your total income = {res}")


# x_man = Position('Pavel', 'Podymov', 'Director', 10, 500)
# print(x_man.name)
# print(x_man.surname)
# print(x_man.position)
# # print(x_man._income)
# x_man.get_full_name()
# x_man.get_total_income()
