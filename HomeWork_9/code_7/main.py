"""Create class CAR"""


class Car:
    """Class Car"""

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_ahead(self):
        """go_ahead"""
        return f'\nYour {self.name} is {self.color} and go ahead.'

    def stop(self):
        """stop"""
        return f'\nYour {self.name} is stopped.'

    def turn(self, direction):
        """direction"""
        return f'\nYour {self.name} is turned {direction}.'

    def show_speed(self):
        """show speed"""
        return f'\nYour speed is {self.speed}! WOW WOW!'


class TownCar(Car):
    """class TownCar"""

    # def __init__(self, speed, color, name, is_police=False):
    #     super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        """show speed"""
        if self.speed > 60:
            res = f'\nYour speed is {self.speed}! You are moving too fast!'
        else:
            res = f"\nYour speed is {self.speed}! It's normal"
        return res


class SportCar(Car):
    """class SportCar"""
    # pass - без pass программа работает


class WorkCar(Car):
    """class WorkCar"""

    # def __init__(self, speed, color, name, is_police=False):
    #     super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        """show speed"""
        if self.speed > 40:
            res = f'\nYour speed is {self.speed}! You are moving too fast!'
        else:
            res = f"\nYour speed is {self.speed}! It's normal!"
        return res


class PoliceCar(Car):
    """class PoliceCar"""
    # pass - не писать, такой вариант предлагает Pylint
    # pass - без pass программа работает


town_1 = TownCar(61, 'green', 'Lada', False)
# print(town_1.go_ahead(), town_1.show_speed(), town_1.turn('left'), town_1.stop())
#
# town_2 = TownCar(60, 'red', 'Lada', False)
# print(town_2.go_ahead(), town_2.show_speed(), town_2.turn('right'), town_2.stop())
#
# sport = SportCar(170, 'blue', 'Volkswagen', False)
# print(sport.go_ahead(), sport.show_speed(), sport.turn('left'), sport.stop())
#
# work_1 = WorkCar(41, 'red', 'Hyundai', False)
# print(work_1.go_ahead(), work_1.show_speed(), work_1.turn('right'), work_1.stop())
#
# work_2 = WorkCar(40, 'red', 'Hyundai', False)
# print(work_2.go_ahead(), work_2.show_speed(), work_2.turn('right'), work_2.stop())
#
# police = PoliceCar(100, 'white_blue', 'Audi', True)
# print(police.go_ahead(), police.show_speed(), police.turn('right'), police.stop())
