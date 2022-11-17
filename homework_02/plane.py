"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption ,  max_cargo):
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, cargo):
        if (cargo + self.cargo) <= self.max_cargo:
            self.cargo = self.cargo + cargo
            return self.cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        dist = self.cargo
        self.cargo = 0
        return dist

