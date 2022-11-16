"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import exceptions
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo = None
    max_cargo = None

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo
        super.__init__(weight=0, fuel=0, fuel_consumption=0)

    def load_cargo(self, cargo):
        self.max_cargo = self.cargo + cargo
        if cargo < self.max_cargo:
            return self.max_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self, cargo):
        cargo = self.cargo - cargo
        return cargo
