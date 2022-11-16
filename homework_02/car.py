"""
создайте класс `Car`, наследник `Vehicle`
"""
from dataclasses import dataclass
from homework_02.base import Vehicle
from homework_02.engine import Engine


@dataclass(Engine)
class Car(Vehicle):
    engine = None

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        super().__init__(weight=0, fuel=0, fuel_consumption=0, )
        pass

    @classmethod
    def set_engine(cls, value):
        pass




#car1 = Car()
#print(car1.__dict__)
