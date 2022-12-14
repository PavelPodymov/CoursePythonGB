"""main fail"""
from car import TownCar, SportCar, WorkCar, PoliceCar

town_1 = TownCar(61, 'green', 'Lada', False)
print(town_1.go_ahead(), town_1.show_speed(), town_1.turn('left'), town_1.stop())

town_2 = TownCar(60, 'red', 'Lada', False)
print(town_2.go_ahead(), town_2.show_speed(), town_2.turn('right'), town_2.stop())

sport = SportCar(170, 'blue', 'Volkswagen', False)
print(sport.go_ahead(), sport.show_speed(), sport.turn('left'), sport.stop())

work_1 = WorkCar(41, 'red', 'Hyundai', False)
print(work_1.go_ahead(), work_1.show_speed(), work_1.turn('right'), work_1.stop())

work_2 = WorkCar(40, 'red', 'Hyundai', False)
print(work_2.go_ahead(), work_2.show_speed(), work_2.turn('right'), work_2.stop())

police = PoliceCar(100, 'white_blue', 'Audi', True)
print(police.go_ahead(), police.show_speed(), police.turn('right'), police.stop())
