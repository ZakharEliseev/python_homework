from _tracemalloc import start

from homework_02 import exceptions
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(LowFuelError, NotEnoughFuel):
    started = False

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, started=None):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is True:
            pass
        elif self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance=0):
        max_distance = self.fuel // self.fuel_consumption
        if max_distance >= distance:
            self.fuel = self.fuel - (distance * self.fuel_consumption)
            return self.fuel
        else:
            raise exceptions.NotEnoughFuel


#v = Vehicle(weight=0, fuel=100, fuel_consumption=10, started=True)
#print(v.move(9))