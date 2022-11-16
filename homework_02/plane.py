"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo = None

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self):
        pass

    def remove_all_cargo(self):
        pass
