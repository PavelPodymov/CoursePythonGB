"""Create class TrafficLight"""
# import random
from time import sleep


class TrafficLight:
    """Create class TrafficLight"""

    def __init__(self):
        self.__color = {"red": 7, "yellow": 2, "green": 4}

    def running(self):
        """print color"""
        i = 2  # random.randint(0, 2)
        if i == 0:
            for k, val in self.__color.items():
                print(k)
                sleep(val)
        else:
            print(f"Color is: [{list(self.__color)[i]}] it's not right working mode")

    @staticmethod
    def jogging():
        """print something"""
        return None


t = TrafficLight()
# t.running()
